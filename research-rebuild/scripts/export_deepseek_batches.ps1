param(
    [string]$CorpusPath = (Join-Path $PSScriptRoot '..\..\sooon-q9adg-articles-v2.jsonl'),
    [string]$OutputDir = (Join-Path $PSScriptRoot '..\deepseek-batches'),
    [int]$MaxArticles = 8,
    [int]$MaxBodyChars = 10000
)

$ErrorActionPreference = 'Stop'

if ($MaxArticles -lt 1) { throw 'MaxArticles must be at least 1.' }
if ($MaxBodyChars -lt 1) { throw 'MaxBodyChars must be at least 1.' }

$CorpusPath = [IO.Path]::GetFullPath($CorpusPath)
$OutputDir = [IO.Path]::GetFullPath($OutputDir)

# Never overwrite an existing export. The caller must choose a new empty directory.
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

if (-not (Test-Path -LiteralPath $CorpusPath -PathType Leaf)) {
    throw "Corpus file not found: $CorpusPath"
}

$sha = (Get-FileHash -LiteralPath $CorpusPath -Algorithm SHA256).Hash.ToUpperInvariant()
$sourceItems = [Collections.Generic.List[object]]::new()
$sourceByOrdinal = @{}
$sourceById = @{}
$sourceLine = 0

foreach ($line in [IO.File]::ReadLines($CorpusPath)) {
    $sourceLine++
    if ([string]::IsNullOrWhiteSpace($line)) {
        throw "Blank line in JSONL corpus at source ordinal $sourceLine."
    }
    try {
        $item = $line | ConvertFrom-Json -Depth 100
    }
    catch {
        throw "Invalid JSON at source ordinal $sourceLine`: $($_.Exception.Message)"
    }
    $id = [string]$item.id
    if ([string]::IsNullOrWhiteSpace($id)) {
        throw "Missing article id at source ordinal $sourceLine."
    }
    if ($sourceById.ContainsKey($id)) {
        throw "Duplicate article id in corpus: $id"
    }
    $entry = [pscustomobject]@{
        source_ordinal = $sourceLine
        item = $item
    }
    $sourceItems.Add($entry)
    $sourceByOrdinal[$sourceLine] = $entry
    $sourceById[$id] = $entry
}

if ($sourceItems.Count -ne 4296) {
    throw "Expected 4296 corpus articles, found $($sourceItems.Count)."
}

# reading_ordinal is computed from the original corpus, independently of any
# existing export: publishedAt ascending, then id ascending as a fixed tie-breaker.
$sortedItems = @(
    $sourceItems |
        Sort-Object `
            @{ Expression = { [int64]$_.item.publishedAt }; Ascending = $true }, `
            @{ Expression = { [string]$_.item.id }; Ascending = $true }
)

$records = [Collections.Generic.List[object]]::new()
$batches = [Collections.Generic.List[object]]::new()
$currentRows = [Collections.Generic.List[object]]::new()
$currentBodyChars = [int64]0
$batchNo = 0

function New-SerializedBatch {
    param(
        [Parameter(Mandatory = $true)]
        [object[]]$Rows,
        [Parameter(Mandatory = $true)]
        [int]$BatchNumber,
        [Parameter(Mandatory = $true)]
        [string]$CorpusSha
    )

    if ($Rows.Count -lt 1) { throw 'Cannot serialize an empty batch.' }
    $batchId = 'r001-b{0:d4}' -f $BatchNumber
    $lines = [Collections.Generic.List[string]]::new()
    foreach ($row in $Rows) {
        $row.batch_id = $batchId
        $payload = [ordered]@{
            batch_id = $batchId
            corpus_sha256 = $CorpusSha
            body_chars = [int64]$row.body_chars
            bodyChars = [int64]$row.body_chars
            oversize = [bool]$row.oversize
            article = $row.article
        }
        # Serialize completely before any output directory is created or written.
        $lines.Add(($payload | ConvertTo-Json -Depth 100 -Compress))
    }

    $bodyChars = [int64](($Rows | ForEach-Object { [int64]$_.body_chars } | Measure-Object -Sum).Sum)
    $sourceOrdinals = @($Rows | ForEach-Object { [int]$_.article.source_ordinal })
    $readingOrdinals = @($Rows | ForEach-Object { [int]$_.article.reading_ordinal })
    $ids = @($Rows | ForEach-Object { [string]$_.article.id })
    $oversizeRows = @($Rows | Where-Object { $_.oversize })

    return [pscustomobject][ordered]@{
        batch_id = $batchId
        file = "$batchId.jsonl"
        lines = @($lines.ToArray())
        article_count = $Rows.Count
        body_chars = $bodyChars
        bodyChars = $bodyChars
        source_ordinals = $sourceOrdinals
        reading_ordinals = $readingOrdinals
        ids = $ids
        oversize_count = $oversizeRows.Count
    }
}

function Flush-CurrentBatch {
    param()
    if ($currentRows.Count -eq 0) { return }
    $script:batchNo++
    $batch = New-SerializedBatch -Rows @($currentRows.ToArray()) -BatchNumber $script:batchNo -CorpusSha $sha
    $batches.Add($batch)
    $currentRows.Clear()
    $script:currentBodyChars = [int64]0
}

for ($i = 0; $i -lt $sortedItems.Count; $i++) {
    $entry = $sortedItems[$i]
    $item = $entry.item
    $text = [string]$item.text
    $bodyChars = [int64]$text.Length # .NET String.Length is UTF-16 code units.
    $readingOrdinal = $i + 1
    $isOversize = $bodyChars -gt $MaxBodyChars

    if ($currentRows.Count -gt 0 -and (
            $currentRows.Count -ge $MaxArticles -or
            ($currentBodyChars + $bodyChars) -gt $MaxBodyChars
        )) {
        Flush-CurrentBatch
    }

    $record = [pscustomobject][ordered]@{
        batch_id = $null
        body_chars = $bodyChars
        bodyChars = $bodyChars
        oversize = $isOversize
        article = [ordered]@{
            source_ordinal = [int]$entry.source_ordinal
            reading_ordinal = [int]$readingOrdinal
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
    }
    $records.Add($record)
    $currentRows.Add($record)
    $currentBodyChars += $bodyChars

    # An over-limit article must be alone in its batch and is marked explicitly.
    if ($isOversize) {
        Flush-CurrentBatch
    }
}
Flush-CurrentBatch

if ($records.Count -ne 4296) {
    throw "Internal export record count is $($records.Count), expected 4296."
}

# Parse the serialized lines and verify the complete export before writing it.
$emittedRows = [Collections.Generic.List[object]]::new()
foreach ($batch in $batches) {
    if ($batch.article_count -gt $MaxArticles) {
        throw "Batch $($batch.batch_id) exceeds article limit: $($batch.article_count)."
    }
    if ($batch.oversize_count -gt 0 -and $batch.article_count -ne 1) {
        throw "Oversize article is not alone in batch $($batch.batch_id)."
    }
    if ($batch.oversize_count -eq 0 -and $batch.body_chars -gt $MaxBodyChars) {
        throw "Batch $($batch.batch_id) exceeds UTF-16 body limit: $($batch.body_chars)."
    }
    foreach ($line in $batch.lines) {
        $obj = $line | ConvertFrom-Json -Depth 100
        if ([string]$obj.batch_id -ne [string]$batch.batch_id) {
            throw "Serialized batch id mismatch in $($batch.file)."
        }
        if ([string]$obj.corpus_sha256 -ne $sha) {
            throw "Corpus hash mismatch in $($batch.file)."
        }
        if ($null -eq $obj.body_chars) {
            throw "Missing body_chars in $($batch.file)."
        }
        $emittedRows.Add($obj)
    }
}

if ($emittedRows.Count -ne 4296) {
    throw "Serialized export contains $($emittedRows.Count) articles, expected 4296."
}

$seenIds = @{}
$expectedBodyChars = [int64](($records | ForEach-Object { [int64]$_.body_chars } | Measure-Object -Sum).Sum)
$actualBodyChars = [int64](($emittedRows | ForEach-Object { [int64]$_.body_chars } | Measure-Object -Sum).Sum)
if ($actualBodyChars -ne $expectedBodyChars) {
    throw "Body character total mismatch: emitted $actualBodyChars, expected $expectedBodyChars."
}

for ($i = 0; $i -lt $emittedRows.Count; $i++) {
    $article = $emittedRows[$i].article
    $expectedEntry = $sortedItems[$i]
    $expectedReadingOrdinal = $i + 1
    $id = [string]$article.id
    if ($seenIds.ContainsKey($id)) {
        throw "Duplicate emitted article id: $id"
    }
    $seenIds[$id] = $true
    if ([int]$article.reading_ordinal -ne $expectedReadingOrdinal) {
        throw "Reading ordinal mismatch for $id`: $($article.reading_ordinal), expected $expectedReadingOrdinal."
    }
    if ([int]$article.source_ordinal -ne [int]$expectedEntry.source_ordinal) {
        throw "Source ordinal mismatch for $id."
    }
    if ($id -ne [string]$expectedEntry.item.id) {
        throw "ID/order mismatch at reading ordinal $expectedReadingOrdinal."
    }
    $sourceEntry = $sourceByOrdinal[[int]$article.source_ordinal]
    if ($null -eq $sourceEntry -or [string]$sourceEntry.item.id -ne $id) {
        throw "Source ordinal $($article.source_ordinal) does not resolve to $id."
    }
    $expectedArticleBodyChars = [int64]([string]$sourceEntry.item.text).Length
    if ([int64]$emittedRows[$i].body_chars -ne $expectedArticleBodyChars) {
        throw "Body character mismatch for $id."
    }
}

if ($seenIds.Count -ne $sourceById.Count) {
    throw "Emitted ID set does not equal corpus ID set."
}
foreach ($id in $sourceById.Keys) {
    if (-not $seenIds.ContainsKey([string]$id)) {
        throw "Missing emitted article id: $id"
    }
}

$oversizeManifest = @(
    $emittedRows |
        Where-Object { $_.oversize } |
        ForEach-Object {
            [ordered]@{
                reading_ordinal = [int]$_.article.reading_ordinal
                source_ordinal = [int]$_.article.source_ordinal
                id = [string]$_.article.id
                body_chars = [int64]$_.body_chars
            }
        }
)

$batchManifest = @(
    $batches | ForEach-Object {
        [ordered]@{
            file = $_.file
            batch_id = $_.batch_id
            article_count = [int]$_.article_count
            body_chars = [int64]$_.body_chars
            bodyChars = [int64]$_.body_chars
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
    schema_version = 'deepseek-batches-v1'
    generated_at = (Get-Date).ToString('o')
    corpus_path = $CorpusPath
    corpus_sha256 = $sha
    record_count = [int]$emittedRows.Count
    article_count = [int]$emittedRows.Count
    first_reading_ordinal = 1
    last_reading_ordinal = [int]$emittedRows.Count
    first_source_ordinal = 1
    last_source_ordinal = [int]$sourceItems.Count
    total_body_chars = $actualBodyChars
    total_text_chars = $actualBodyChars
    max_articles = $MaxArticles
    max_body_chars = $MaxBodyChars
    batch_count = [int]$batches.Count
    oversize_articles = $oversizeManifest
    batches = $batchManifest
    validation = [ordered]@{
        ids_exactly_once = $true
        reading_ordinals_contiguous = $true
        source_ordinals_match_corpus = $true
        utf16_body_chars_verified = $true
    }
    status = 'PASS'
}

# All records and the manifest are serialized before the output directory is created.
if (-not (Test-Path -LiteralPath $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir -Force | Out-Null
}
$utf8NoBom = [Text.UTF8Encoding]::new($false)
foreach ($batch in $batches) {
    $batchPath = Join-Path $OutputDir $batch.file
    [IO.File]::WriteAllLines($batchPath, [string[]]$batch.lines, $utf8NoBom)
}
$manifestPath = Join-Path $OutputDir 'manifest.json'
$manifestJson = $manifest | ConvertTo-Json -Depth 20
[IO.File]::WriteAllText($manifestPath, $manifestJson, $utf8NoBom)

Get-ChildItem -LiteralPath $OutputDir -Filter 'r001-b*.jsonl' -File | Sort-Object Name | Select-Object -ExpandProperty FullName
