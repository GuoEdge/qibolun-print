param(
    [string]$CorpusPath = (Join-Path $PSScriptRoot '..\..\sooon-q9adg-articles-v2.jsonl'),
    [string]$BaselineDir = (Join-Path $PSScriptRoot '..\deepseek-batches'),
    [string]$OutputDir = (Join-Path $PSScriptRoot '..\deepseek-batches-incremental-20260923'),
    [string]$BatchPrefix = 'r002',
    [int]$MaxArticles = 8,
    [int]$MaxBodyChars = 10000
)

$ErrorActionPreference = 'Stop'

if ($MaxArticles -lt 1) { throw 'MaxArticles must be at least 1.' }
if ($MaxBodyChars -lt 1) { throw 'MaxBodyChars must be at least 1.' }
if ([string]::IsNullOrWhiteSpace($BatchPrefix)) { throw 'BatchPrefix must not be empty.' }

$CorpusPath = [IO.Path]::GetFullPath($CorpusPath)
$BaselineDir = [IO.Path]::GetFullPath($BaselineDir)
$OutputDir = [IO.Path]::GetFullPath($OutputDir)

if (-not (Test-Path -LiteralPath $CorpusPath -PathType Leaf)) {
    throw "Corpus file not found: $CorpusPath"
}
if (-not (Test-Path -LiteralPath $BaselineDir -PathType Container)) {
    throw "Baseline directory not found: $BaselineDir"
}
$baselineManifestPath = Join-Path $BaselineDir 'manifest.json'
if (-not (Test-Path -LiteralPath $baselineManifestPath -PathType Leaf)) {
    throw "Baseline manifest not found: $baselineManifestPath"
}
if (Test-Path -LiteralPath $OutputDir) {
    $outputItem = Get-Item -LiteralPath $OutputDir -Force
    if (-not $outputItem.PSIsContainer) {
        throw "Output path exists but is not a directory: $OutputDir"
    }
    $existingEntries = @(Get-ChildItem -LiteralPath $OutputDir -Force)
    if ($existingEntries.Count -gt 0) {
        throw "Output directory must be empty; refusing to overwrite: $OutputDir"
    }
}

function Get-Sha256Hex {
    param([Parameter(Mandatory = $true)][string]$Text)
    $sha = [Security.Cryptography.SHA256]::Create()
    try {
        $bytes = [Text.Encoding]::UTF8.GetBytes($Text)
        $digest = $sha.ComputeHash($bytes)
    }
    finally {
        $sha.Dispose()
    }
    return ([BitConverter]::ToString($digest) -replace '-', '').ToUpperInvariant()
}

function Get-ArticleFingerprint {
    param([Parameter(Mandatory = $true)][object]$Article)
    # Source ordinals are intentionally excluded: adding rows to the source
    # JSONL shifts later source line numbers without changing an article.
    $canonical = [ordered]@{
        id = [string]$Article.id
        title = [string]$Article.title
        url = [string]$Article.url
        publishedAt = [string]$Article.publishedAt
        updatedAt = [string]$Article.updatedAt
        question = [string]$Article.question
        brief = [string]$Article.brief
        text = [string]$Article.text
        lexical = [string]$Article.lexical
        # Keep nested provenance/superseded objects as objects in the
        # fingerprint; casting them to [string] would lose their contents.
        provenance = $Article.provenance
        superseded = $Article.superseded
    }
    $json = $canonical | ConvertTo-Json -Depth 100 -Compress
    return Get-Sha256Hex -Text $json
}

$utf8NoBom = [Text.UTF8Encoding]::new($false)
$corpusSha = (Get-FileHash -LiteralPath $CorpusPath -Algorithm SHA256).Hash.ToUpperInvariant()
$baselineManifest = Get-Content -LiteralPath $baselineManifestPath -Raw -Encoding utf8 | ConvertFrom-Json -Depth 100
$baselineSha = [string]$baselineManifest.corpus_sha256
$baselineExpectedCount = [int]$baselineManifest.record_count
$baselineBatchEntries = @($baselineManifest.batches)
if ($baselineExpectedCount -lt 1 -or $baselineBatchEntries.Count -lt 1) {
    throw 'Baseline manifest has no usable records or batches.'
}

# Read the baseline export, not the old source line numbers. This makes the
# append-only comparison safe when new records were inserted before old rows.
$baselineById = @{}
$baselineRowCount = 0
foreach ($batchEntry in $baselineBatchEntries) {
    $batchPath = Join-Path $BaselineDir ([string]$batchEntry.file)
    if (-not (Test-Path -LiteralPath $batchPath -PathType Leaf)) {
        throw "Baseline batch missing: $batchPath"
    }
    foreach ($line in [IO.File]::ReadLines($batchPath, $utf8NoBom)) {
        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        $payload = $line | ConvertFrom-Json -Depth 100
        $article = $payload.article
        $id = [string]$article.id
        if ([string]::IsNullOrWhiteSpace($id)) { throw "Baseline row has no article id: $batchPath" }
        if ($baselineById.ContainsKey($id)) { throw "Duplicate baseline article id: $id" }
        $baselineById[$id] = $article
        $baselineRowCount++
    }
}
if ($baselineRowCount -ne $baselineExpectedCount) {
    throw "Baseline row count mismatch: manifest=$baselineExpectedCount, files=$baselineRowCount."
}

# Read the current corpus once, retaining both source ordinal and article.
$currentItems = [Collections.Generic.List[object]]::new()
$currentById = @{}
$sourceOrdinal = 0
foreach ($line in [IO.File]::ReadLines($CorpusPath, $utf8NoBom)) {
    $sourceOrdinal++
    if ([string]::IsNullOrWhiteSpace($line)) { throw "Blank line in corpus at source ordinal $sourceOrdinal." }
    $item = $line | ConvertFrom-Json -Depth 100
    $id = [string]$item.id
    if ([string]::IsNullOrWhiteSpace($id)) { throw "Missing article id at source ordinal $sourceOrdinal." }
    if ($currentById.ContainsKey($id)) { throw "Duplicate current article id: $id" }
    $entry = [pscustomobject]@{ source_ordinal = $sourceOrdinal; item = $item }
    [void]$currentItems.Add($entry)
    $currentById[$id] = $entry
}

if ($currentItems.Count -lt $baselineRowCount) {
    throw "Current corpus is smaller than baseline: current=$($currentItems.Count), baseline=$baselineRowCount."
}

# Fail closed if an existing article changed. The incremental package is only
# valid for a new-record delta; changed old records require a fresh full export.
$missingBaselineIds = [Collections.Generic.List[string]]::new()
$changedBaselineIds = [Collections.Generic.List[string]]::new()
foreach ($id in $baselineById.Keys) {
    if (-not $currentById.ContainsKey($id)) {
        [void]$missingBaselineIds.Add([string]$id)
        continue
    }
    $oldFingerprint = Get-ArticleFingerprint -Article $baselineById[$id]
    $newFingerprint = Get-ArticleFingerprint -Article $currentById[$id].item
    if ($oldFingerprint -ne $newFingerprint) { [void]$changedBaselineIds.Add([string]$id) }
}
if ($missingBaselineIds.Count -gt 0) {
    throw "Baseline IDs missing from current corpus ($($missingBaselineIds.Count)); refusing incremental export."
}
if ($changedBaselineIds.Count -gt 0) {
    throw "Existing baseline articles changed ($($changedBaselineIds.Count)); run a full export instead. IDs: $($changedBaselineIds -join ', ')"
}

# Recompute stable reading ordinals from the current corpus. This is the same
# publishedAt-then-ID ordering used by export_deepseek_batches.ps1.
$sortedItems = @(
    $currentItems |
        Sort-Object `
            @{ Expression = { [int64]$_.item.publishedAt }; Ascending = $true }, `
            @{ Expression = { [string]$_.item.id }; Ascending = $true }
)
$readingById = @{}
$readingOrdinal = 0
foreach ($entry in $sortedItems) {
    $readingOrdinal++
    $readingById[[string]$entry.item.id] = $readingOrdinal
}

$newEntries = @(
    $sortedItems | Where-Object { -not $baselineById.ContainsKey([string]$_.item.id) }
)
if ($newEntries.Count -eq 0) {
    throw 'No new article IDs found; no incremental export is needed.'
}

$currentRows = [Collections.Generic.List[object]]::new()
$batches = [Collections.Generic.List[object]]::new()
$currentBodyChars = [int64]0
$batchNo = 0

function Flush-IncrementalBatch {
    param([Parameter(Mandatory = $true)][object[]]$Rows)
    if ($Rows.Count -eq 0) { return }
    $script:batchNo++
    $batchId = '{0}-b{1:d4}' -f $BatchPrefix, $script:batchNo
    $lines = [Collections.Generic.List[string]]::new()
    foreach ($row in $Rows) {
        $row.batch_id = $batchId
        $payload = [ordered]@{
            batch_id = $batchId
            corpus_sha256 = $corpusSha
            body_chars = [int64]$row.body_chars
            bodyChars = [int64]$row.body_chars
            oversize = [bool]$row.oversize
            article = $row.article
        }
        [void]$lines.Add(($payload | ConvertTo-Json -Depth 100 -Compress))
    }
    $bodyChars = [int64](($Rows | ForEach-Object { [int64]$_.body_chars } | Measure-Object -Sum).Sum)
    $sourceOrdinals = @($Rows | ForEach-Object { [int]$_.article.source_ordinal })
    $readingOrdinals = @($Rows | ForEach-Object { [int]$_.article.reading_ordinal })
    $ids = @($Rows | ForEach-Object { [string]$_.article.id })
    $oversizeCount = @($Rows | Where-Object { $_.oversize }).Count
    [void]$script:batches.Add([pscustomobject][ordered]@{
        file = "$batchId.jsonl"
        batch_id = $batchId
        article_count = [int]$Rows.Count
        body_chars = $bodyChars
        bodyChars = $bodyChars
        source_ordinals = $sourceOrdinals
        reading_ordinals = $readingOrdinals
        ids = $ids
        oversize_count = [int]$oversizeCount
        lines = @($lines.ToArray())
    })
}

foreach ($entry in $newEntries) {
    $item = $entry.item
    $bodyChars = [int64]([string]$item.text).Length
    $isOversize = $bodyChars -gt $MaxBodyChars
    if ($currentRows.Count -gt 0 -and (
            $currentRows.Count -ge $MaxArticles -or
            ($currentBodyChars + $bodyChars) -gt $MaxBodyChars
        )) {
        Flush-IncrementalBatch -Rows @($currentRows.ToArray())
        $currentRows.Clear()
        $currentBodyChars = [int64]0
    }
    $article = [ordered]@{
        source_ordinal = [int]$entry.source_ordinal
        reading_ordinal = [int]$readingById[[string]$item.id]
        id = [string]$item.id
        title = $item.title
        url = $item.url
        publishedAt = $item.publishedAt
        updatedAt = $item.updatedAt
        question = $item.question
        brief = $item.brief
        text = $item.text
        lexical = $item.lexical
        provenance = $item.provenance
        superseded = $item.superseded
    }
    [void]$currentRows.Add([pscustomobject][ordered]@{
        batch_id = $null
        body_chars = $bodyChars
        oversize = $isOversize
        article = $article
    })
    $currentBodyChars += $bodyChars
    if ($isOversize) {
        Flush-IncrementalBatch -Rows @($currentRows.ToArray())
        $currentRows.Clear()
        $currentBodyChars = [int64]0
    }
}
if ($currentRows.Count -gt 0) {
    Flush-IncrementalBatch -Rows @($currentRows.ToArray())
    $currentRows.Clear()
}

# Validate all serialized rows before creating the output directory.
$emitted = [Collections.Generic.List[object]]::new()
foreach ($batch in $batches) {
    if ($batch.article_count -gt $MaxArticles) { throw "Batch $($batch.batch_id) exceeds MaxArticles." }
    if ($batch.oversize_count -gt 0 -and $batch.article_count -ne 1) { throw "Oversize article is not alone in $($batch.batch_id)." }
    if ($batch.oversize_count -eq 0 -and $batch.body_chars -gt $MaxBodyChars) { throw "Batch $($batch.batch_id) exceeds MaxBodyChars." }
    foreach ($line in $batch.lines) {
        $obj = $line | ConvertFrom-Json -Depth 100
        if ([string]$obj.batch_id -ne [string]$batch.batch_id) { throw "Batch ID mismatch in $($batch.file)." }
        if ([string]$obj.corpus_sha256 -ne $corpusSha) { throw "Corpus hash mismatch in $($batch.file)." }
        [void]$emitted.Add($obj)
    }
}
if ($emitted.Count -ne $newEntries.Count) {
    throw "Incremental serialized count mismatch: emitted=$($emitted.Count), new=$($newEntries.Count)."
}
$seenIds = @{}
foreach ($obj in $emitted) {
    $id = [string]$obj.article.id
    if ($seenIds.ContainsKey($id)) { throw "Duplicate incremental article id: $id" }
    $seenIds[$id] = $true
    if ($baselineById.ContainsKey($id)) { throw "Incremental row overlaps baseline ID: $id" }
    if (-not $currentById.ContainsKey($id)) { throw "Incremental row is absent from current corpus: $id" }
    $entry = $currentById[$id]
    if ([int]$obj.article.source_ordinal -ne [int]$entry.source_ordinal) { throw "Source ordinal mismatch for $id." }
    if ([int]$obj.article.reading_ordinal -ne [int]$readingById[$id]) { throw "Reading ordinal mismatch for $id." }
    if ([int64]$obj.body_chars -ne [int64]([string]$entry.item.text).Length) { throw "Body chars mismatch for $id." }
}
foreach ($entry in $newEntries) {
    $id = [string]$entry.item.id
    if (-not $seenIds.ContainsKey($id)) { throw "Missing incremental article ID: $id" }
}

$newManifestArticles = @(
    $newEntries | ForEach-Object {
        $id = [string]$_.item.id
        [ordered]@{
            source_ordinal = [int]$_.source_ordinal
            reading_ordinal = [int]$readingById[$id]
            id = $id
            title = [string]$_.item.title
            body_chars = [int64]([string]$_.item.text).Length
        }
    }
)
$manifestBatches = @(
    $batches | ForEach-Object {
        [ordered]@{
            file = $_.file
            batch_id = $_.batch_id
            article_count = [int]$_.article_count
            body_chars = [int64]$_.body_chars
            bodyChars = [int64]$_.bodyChars
            first_reading_ordinal = [int]($_.reading_ordinals | Measure-Object -Minimum).Minimum
            last_reading_ordinal = [int]($_.reading_ordinals | Measure-Object -Maximum).Maximum
            first_source_ordinal = [int]($_.source_ordinals | Measure-Object -Minimum).Minimum
            last_source_ordinal = [int]($_.source_ordinals | Measure-Object -Maximum).Maximum
            source_ordinals = @($_.source_ordinals)
            reading_ordinals = @($_.reading_ordinals)
            ids = @($_.ids)
            oversize_count = [int]$_.oversize_count
        }
    }
)
$manifest = [ordered]@{
    schema_version = 'deepseek-batches-incremental-v1'
    generated_at = (Get-Date).ToString('o')
    corpus_path = $CorpusPath
    corpus_sha256 = $corpusSha
    current_record_count = [int]$currentItems.Count
    baseline_dir = $BaselineDir
    baseline_manifest = $baselineManifestPath
    baseline_corpus_sha256 = $baselineSha
    baseline_record_count = [int]$baselineRowCount
    baseline_batch_count = [int]$baselineBatchEntries.Count
    incremental_record_count = [int]$newEntries.Count
    incremental_source_ordinals = @($newManifestArticles | ForEach-Object { [int]$_.source_ordinal })
    incremental_reading_ordinals = @($newManifestArticles | ForEach-Object { [int]$_.reading_ordinal })
    max_articles = $MaxArticles
    max_body_chars = $MaxBodyChars
    batch_prefix = $BatchPrefix
    batch_count = [int]$batches.Count
    new_articles = $newManifestArticles
    batches = $manifestBatches
    validation = [ordered]@{
        baseline_ids_present = $true
        existing_articles_unchanged = $true
        incremental_ids_exactly_once = $true
        current_corpus_hash_verified = $true
        utf16_body_chars_verified = $true
    }
    status = 'PASS'
}

if (-not (Test-Path -LiteralPath $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}
foreach ($batch in $batches) {
    [IO.File]::WriteAllLines((Join-Path $OutputDir $batch.file), [string[]]$batch.lines, $utf8NoBom)
}
[IO.File]::WriteAllText((Join-Path $OutputDir 'manifest.json'), ($manifest | ConvertTo-Json -Depth 100), $utf8NoBom)

Write-Output "status=PASS"
Write-Output "baseline_records=$baselineRowCount current_records=$($currentItems.Count) incremental_records=$($newEntries.Count)"
Write-Output "incremental_batches=$($batches.Count) output_dir=$OutputDir"
foreach ($batch in $manifestBatches) {
    Write-Output ("{0}: articles={1} body_chars={2} reading={3}-{4}" -f $batch.batch_id, $batch.article_count, $batch.body_chars, $batch.first_reading_ordinal, $batch.last_reading_ordinal)
}
