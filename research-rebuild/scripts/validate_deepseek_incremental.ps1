param(
    [string]$IncrementalDir = (Join-Path $PSScriptRoot '..\deepseek-batches-incremental-20260923'),
    [string]$CorpusPath = (Join-Path $PSScriptRoot '..\..\sooon-q9adg-articles-v2.jsonl'),
    [string]$BaselineDir = (Join-Path $PSScriptRoot '..\deepseek-batches'),
    [string]$ReportPath = ''
)

$ErrorActionPreference = 'Stop'
$IncrementalDir = [IO.Path]::GetFullPath($IncrementalDir)
$CorpusPath = [IO.Path]::GetFullPath($CorpusPath)
$BaselineDir = [IO.Path]::GetFullPath($BaselineDir)
if ([string]::IsNullOrWhiteSpace($ReportPath)) {
    $ReportPath = Join-Path $IncrementalDir 'validation-report.json'
}
$ReportPath = [IO.Path]::GetFullPath($ReportPath)

$failures = [Collections.Generic.List[string]]::new()
function Fail([string]$Message) { [void]$script:failures.Add($Message) }

function Get-Sha256Hex {
    param([Parameter(Mandatory = $true)][string]$Text)
    $sha = [Security.Cryptography.SHA256]::Create()
    try {
        $digest = $sha.ComputeHash([Text.Encoding]::UTF8.GetBytes($Text))
    }
    finally { $sha.Dispose() }
    return ([BitConverter]::ToString($digest) -replace '-', '').ToUpperInvariant()
}

function Get-ArticleFingerprint {
    param([Parameter(Mandatory = $true)][object]$Article)
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
        provenance = $Article.provenance
        superseded = $Article.superseded
    }
    return Get-Sha256Hex -Text ($canonical | ConvertTo-Json -Depth 100 -Compress)
}

$utf8NoBom = [Text.UTF8Encoding]::new($false)
if (-not (Test-Path -LiteralPath $IncrementalDir -PathType Container)) { Fail "incremental directory missing: $IncrementalDir" }
if (-not (Test-Path -LiteralPath $CorpusPath -PathType Leaf)) { Fail "corpus missing: $CorpusPath" }
if (-not (Test-Path -LiteralPath $BaselineDir -PathType Container)) { Fail "baseline directory missing: $BaselineDir" }
$manifestPath = Join-Path $IncrementalDir 'manifest.json'
$baselineManifestPath = Join-Path $BaselineDir 'manifest.json'
if (-not (Test-Path -LiteralPath $manifestPath -PathType Leaf)) { Fail "incremental manifest missing: $manifestPath" }
if (-not (Test-Path -LiteralPath $baselineManifestPath -PathType Leaf)) { Fail "baseline manifest missing: $baselineManifestPath" }

$manifest = $null
$baselineManifest = $null
if (Test-Path -LiteralPath $manifestPath -PathType Leaf) {
    try { $manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding utf8 | ConvertFrom-Json -Depth 100 }
    catch { Fail "incremental manifest JSON invalid: $($_.Exception.Message)" }
}
if (Test-Path -LiteralPath $baselineManifestPath -PathType Leaf) {
    try { $baselineManifest = Get-Content -LiteralPath $baselineManifestPath -Raw -Encoding utf8 | ConvertFrom-Json -Depth 100 }
    catch { Fail "baseline manifest JSON invalid: $($_.Exception.Message)" }
}

$baselineById = @{}
$baselineRows = 0
if ($null -ne $baselineManifest) {
    foreach ($b in @($baselineManifest.batches)) {
        $path = Join-Path $BaselineDir ([string]$b.file)
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { Fail "baseline batch missing: $path"; continue }
        foreach ($line in [IO.File]::ReadLines($path, $utf8NoBom)) {
            if ([string]::IsNullOrWhiteSpace($line)) { continue }
            try { $payload = $line | ConvertFrom-Json -Depth 100 }
            catch { Fail "baseline JSON invalid in $path"; continue }
            $id = [string]$payload.article.id
            if ([string]::IsNullOrWhiteSpace($id)) { Fail "baseline row has no id in $path"; continue }
            if ($baselineById.ContainsKey($id)) { Fail "duplicate baseline id: $id" } else { $baselineById[$id] = $payload.article }
            $baselineRows++
        }
    }
    if ([int]$baselineManifest.record_count -ne $baselineRows) { Fail "baseline row count mismatch" }
}

$currentItems = [Collections.Generic.List[object]]::new()
$currentById = @{}
if (Test-Path -LiteralPath $CorpusPath -PathType Leaf) {
    $sourceOrdinal = 0
    foreach ($line in [IO.File]::ReadLines($CorpusPath, $utf8NoBom)) {
        $sourceOrdinal++
        if ([string]::IsNullOrWhiteSpace($line)) { Fail "blank corpus line $sourceOrdinal"; continue }
        try { $item = $line | ConvertFrom-Json -Depth 100 }
        catch { Fail "invalid corpus JSON at source ordinal $sourceOrdinal"; continue }
        $id = [string]$item.id
        if ([string]::IsNullOrWhiteSpace($id)) { Fail "corpus row $sourceOrdinal has no id"; continue }
        if ($currentById.ContainsKey($id)) { Fail "duplicate current id: $id"; continue }
        $entry = [pscustomobject]@{ source_ordinal = $sourceOrdinal; item = $item }
        [void]$currentItems.Add($entry)
        $currentById[$id] = $entry
    }
}

$readingById = @{}
if ($currentItems.Count -gt 0) {
    $sorted = @($currentItems | Sort-Object @{e={ [int64]$_.item.publishedAt };Ascending=$true}, @{e={ [string]$_.item.id };Ascending=$true})
    $reading = 0
    foreach ($entry in $sorted) { $reading++; $readingById[[string]$entry.item.id] = $reading }
}

if ($null -ne $manifest) {
    if ([string]$manifest.schema_version -ne 'deepseek-batches-incremental-v1') { Fail "unexpected incremental schema_version=$($manifest.schema_version)" }
    if ([string]$manifest.status -ne 'PASS') { Fail "manifest status is not PASS" }
    if ([int]$manifest.current_record_count -ne $currentItems.Count) { Fail "current_record_count mismatch" }
    if ([int]$manifest.baseline_record_count -ne $baselineRows) { Fail "baseline_record_count mismatch" }
    if ([int]$manifest.incremental_record_count -ne ($currentItems.Count - $baselineRows)) { Fail "incremental_record_count mismatch" }
    if ((Get-FileHash -LiteralPath $CorpusPath -Algorithm SHA256).Hash.ToUpperInvariant() -ne [string]$manifest.corpus_sha256) { Fail 'current corpus SHA-256 mismatch' }
    if ([string]$manifest.baseline_corpus_sha256 -ne [string]$baselineManifest.corpus_sha256) { Fail 'baseline corpus SHA-256 mismatch' }
}

# Existing baseline records must still be byte-equivalent in content. Source
# ordinals may shift when rows are inserted, so they are not part of this check.
foreach ($id in $baselineById.Keys) {
    if (-not $currentById.ContainsKey($id)) { Fail "baseline id missing from current corpus: $id"; continue }
    if ((Get-ArticleFingerprint $baselineById[$id]) -ne (Get-ArticleFingerprint $currentById[$id].item)) { Fail "existing article changed: $id" }
}

$expectedNewIds = [Collections.Generic.HashSet[string]]::new()
foreach ($entry in $currentItems) {
    $id = [string]$entry.item.id
    if (-not $baselineById.ContainsKey($id)) { [void]$expectedNewIds.Add($id) }
}
$packageIds = [Collections.Generic.HashSet[string]]::new()
$packageRows = 0
if ($null -ne $manifest) {
    foreach ($b in @($manifest.batches)) {
        $path = Join-Path $IncrementalDir ([string]$b.file)
        if (-not (Test-Path -LiteralPath $path -PathType Leaf)) { Fail "incremental batch missing: $path"; continue }
        $lines = @(Get-Content -LiteralPath $path -Encoding utf8 | Where-Object { $_.Trim() })
        if ($lines.Count -ne [int]$b.article_count) { Fail "$($b.batch_id) line count mismatch" }
        $batchBodyChars = [int64]0
        $batchOversize = 0
        foreach ($line in $lines) {
            try { $payload = $line | ConvertFrom-Json -Depth 100 }
            catch { Fail "invalid JSON in $path"; continue }
            $id = [string]$payload.article.id
            $packageRows++
            if ([string]$payload.batch_id -ne [string]$b.batch_id) { Fail "batch id mismatch in $path" }
            if ([string]$payload.corpus_sha256 -ne [string]$manifest.corpus_sha256) { Fail "corpus hash mismatch for $id" }
            if ([string]::IsNullOrWhiteSpace($id)) { Fail "incremental row without id in $path"; continue }
            if (-not $packageIds.Add($id)) { Fail "duplicate incremental id: $id" }
            if (-not $expectedNewIds.Contains($id)) { Fail "row is not a new ID: $id" }
            if (-not $currentById.ContainsKey($id)) { Fail "incremental id absent in current corpus: $id"; continue }
            $entry = $currentById[$id]
            $expectedChars = [int64]([string]$entry.item.text).Length
            $batchBodyChars += [int64]$payload.body_chars
            if ([int64]$payload.body_chars -ne $expectedChars) { Fail "body_chars mismatch for $id" }
            if ([int]$payload.article.source_ordinal -ne [int]$entry.source_ordinal) { Fail "source ordinal mismatch for $id" }
            if ([int]$payload.article.reading_ordinal -ne [int]$readingById[$id]) { Fail "reading ordinal mismatch for $id" }
            if ([string]$payload.article.title -ne [string]$entry.item.title) { Fail "title mismatch for $id" }
            if ([bool]$payload.oversize -ne ($expectedChars -gt [int]$manifest.max_body_chars)) { Fail "oversize flag mismatch for $id" }
            if ([bool]$payload.oversize) { $batchOversize++ }
        }
        if ($batchBodyChars -ne [int64]$b.body_chars) { Fail "$($b.batch_id) body_chars mismatch" }
        if ($batchOversize -ne [int]$b.oversize_count) { Fail "$($b.batch_id) oversize_count mismatch" }
        if ($lines.Count -gt [int]$manifest.max_articles) { Fail "$($b.batch_id) exceeds max_articles" }
        if ($batchOversize -gt 0 -and $lines.Count -ne 1) { Fail "$($b.batch_id) mixes oversize article" }
        if ($batchOversize -eq 0 -and $batchBodyChars -gt [int64]$manifest.max_body_chars) { Fail "$($b.batch_id) exceeds max_body_chars" }
    }
}
if ($null -ne $manifest -and $packageRows -ne [int]$manifest.incremental_record_count) { Fail 'package row count does not equal manifest incremental count' }
if ($packageIds.Count -ne $expectedNewIds.Count) { Fail "package/new ID set size mismatch: package=$($packageIds.Count), expected=$($expectedNewIds.Count)" }
foreach ($id in $expectedNewIds) { if (-not $packageIds.Contains($id)) { Fail "missing new ID from package: $id" } }

$result = [ordered]@{
    generated_at = (Get-Date).ToString('o')
    status = if ($failures.Count -eq 0) { 'PASS' } else { 'FAIL' }
    corpus_path = $CorpusPath
    corpus_sha256 = if ($null -ne $manifest) { [string]$manifest.corpus_sha256 } else { '' }
    baseline_record_count = $baselineRows
    current_record_count = $currentItems.Count
    expected_incremental_records = $expectedNewIds.Count
    package_records = $packageRows
    package_batches = if ($null -ne $manifest) { @($manifest.batches).Count } else { 0 }
    failures = @($failures)
}
$reportDir = Split-Path -Parent $ReportPath
if (-not (Test-Path -LiteralPath $reportDir)) { New-Item -ItemType Directory -Path $reportDir -Force | Out-Null }
[IO.File]::WriteAllText($ReportPath, ($result | ConvertTo-Json -Depth 20), $utf8NoBom)
$result | ConvertTo-Json -Depth 20
if ($failures.Count -gt 0) { exit 1 }
