param(
    [string]$Root = (Join-Path $PSScriptRoot '..')
)
$ErrorActionPreference = 'Stop'
$Root = [IO.Path]::GetFullPath($Root)
$manifest = Get-Content -LiteralPath (Join-Path $Root 'data/corpus-manifest.json') -Raw -Encoding utf8 | ConvertFrom-Json
$index = @(Import-Csv -LiteralPath (Join-Path $Root 'data/article-index.csv') -Encoding utf8)
$reading = @(Get-Content -LiteralPath (Join-Path $Root 'records/reading-records.jsonl') -Encoding utf8 | Where-Object { $_.Trim() } | ForEach-Object { $_ | ConvertFrom-Json -Depth 40 })
$reviews = @(Get-Content -LiteralPath (Join-Path $Root 'records/review-records.jsonl') -Encoding utf8 | Where-Object { $_.Trim() } | ForEach-Object { $_ | ConvertFrom-Json -Depth 20 })
$annotations = @(Get-Content -LiteralPath (Join-Path $Root 'records/calibration-annotations.jsonl') -Encoding utf8 | Where-Object { $_.Trim() } | ForEach-Object { $_ | ConvertFrom-Json -Depth 30 })
$failures = [Collections.Generic.List[string]]::new()
if ($manifest.record_count -ne 4296) { $failures.Add("manifest record_count=$($manifest.record_count)") }
if ($index.Count -ne 4296) { $failures.Add("index rows=$($index.Count)") }
if ($reading.Count -ne 4296) { $failures.Add("reading rows=$($reading.Count)") }
if ($reviews.Count -ne 4296) { $failures.Add("review rows=$($reviews.Count)") }
if (@($index | Group-Object id | Where-Object Count -gt 1).Count -gt 0) { $failures.Add('duplicate IDs in article index') }
if (@($reading | Group-Object id | Where-Object Count -gt 1).Count -gt 0) { $failures.Add('duplicate IDs in reading records') }
$readingIds = [Collections.Generic.HashSet[string]]::new([string[]]$reading.id)
foreach ($row in $index) { if (-not $readingIds.Contains([string]$row.id)) { $failures.Add("missing reading record $($row.id)") } }
foreach ($item in $annotations) {
    $target = $reading | Where-Object id -eq $item.id
    if ($null -eq $target) { $failures.Add("annotation target missing $($item.id)"); continue }
    if ($target.understanding_status -ne 'understanding_complete') { $failures.Add("annotation not merged $($item.id)") }
    foreach ($claim in @($item.main_claims)) {
        foreach ($evidence in @($claim.evidence)) {
            if ([string]$evidence -notmatch '^P\d{3}(-P\d{3})?$') { $failures.Add("bad evidence location $($item.id):$evidence") }
        }
    }
}
$progress = Get-Content -LiteralPath (Join-Path $Root 'reports/progress.json') -Raw -Encoding utf8 | ConvertFrom-Json
$result = [ordered]@{ status = if ($failures.Count -eq 0) { 'PASS' } else { 'FAIL' }; corpus_records = $manifest.record_count; index_records = $index.Count; reading_records = $reading.Count; review_records = $reviews.Count; annotations = $annotations.Count; understanding_complete = @($reading | Where-Object understanding_status -eq 'understanding_complete').Count; independent_review_complete = @($reading | Where-Object review_status -eq 'reviewed').Count; progress_understanding = $progress.understanding_complete; failures = @($failures) }
$result | ConvertTo-Json -Depth 6
if ($failures.Count -gt 0) { exit 1 }
