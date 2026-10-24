param(
    [Parameter(Mandatory = $true)][string]$InputBatch,
    [Parameter(Mandatory = $true)][string]$OutputJsonl,
    [string]$CorpusPath = (Join-Path $PSScriptRoot '..\..\sooon-q9adg-articles-v2.jsonl')
)
$ErrorActionPreference = 'Stop'
$failures = [Collections.Generic.List[string]]::new()
function Fail([string]$Message) { $failures.Add($Message) }

$utf8 = [Text.UTF8Encoding]::new($false)
$inputLines = @([IO.File]::ReadAllLines($InputBatch, $utf8) | Where-Object { $_.Trim() })
$outputLines = @([IO.File]::ReadAllLines($OutputJsonl, $utf8) | Where-Object { $_.Trim() })
$inputRows = @($inputLines | ForEach-Object { try { $_ | ConvertFrom-Json } catch { Fail("input JSON parse: $($_.Exception.Message)"); $null } } | Where-Object { $null -ne $_ })
$outputs = [Collections.Generic.List[object]]::new()
foreach ($line in $outputLines) {
    try { $outputs.Add(($line | ConvertFrom-Json)) }
    catch { Fail("output JSON parse: $($_.Exception.Message)") }
}
if ($outputs.Count -ne $inputRows.Count) { Fail("line count output=$($outputs.Count), input=$($inputRows.Count)") }
$inputMap = @{}
foreach ($r in $inputRows) { $inputMap[[string]$r.article.id] = $r }
$outputIds = @{}
$expectedHash = if ($inputRows.Count) { [string]$inputRows[0].corpus_sha256 } else { '' }
foreach ($r in $outputs) {
    if ([string]$r.record_type -ne 'article_reading') { Fail('record_type must be article_reading') }
    if ([string]$r.schema_version -ne '0.2.0') { Fail("schema_version=$($r.schema_version)") }
    $id = [string]$r.article_id
    if ([string]::IsNullOrWhiteSpace($id)) { Fail('missing article_id'); continue }
    if ($outputIds.ContainsKey($id)) { Fail("duplicate output article_id $id") } else { $outputIds[$id] = $true }
    if (-not $inputMap.ContainsKey($id)) { Fail("output article_id not in input $id"); continue }
    $in = $inputMap[$id]
    if ([string]$r.corpus_sha256 -ne $expectedHash) { Fail("corpus hash mismatch $id") }
    if ([int]$r.source_ordinal -ne [int]$in.article.source_ordinal) { Fail("source_ordinal mismatch $id") }
    if ([int]$r.reading_ordinal -ne [int]$in.article.reading_ordinal) { Fail("reading_ordinal mismatch $id") }
    if ([string]$r.metadata.title -ne [string]$in.article.title) { Fail("title mismatch $id") }
    $status = [string]$r.reading.status
    $full = [bool]$r.structure.full_text_checked
    $imageChecked = [bool]$r.reading.image_checked
    $images = @($r.structure.images)
    if ($status -eq 'read' -and -not $full) { Fail("read without full_text_checked $id") }
    if ($images.Count -gt 0 -and $status -eq 'read' -and -not $imageChecked) { Fail("image article read without image_checked $id") }
    if ($status -in @('blocked','needs_reread') -and [string]::IsNullOrWhiteSpace([string]$r.notes) -and @($r.analysis.unresolved_questions).Count -eq 0) { Fail("blocked/needs_reread without reason $id") }
    $paragraphIds = @{}; foreach ($p in @($r.structure.paragraphs)) { $paragraphIds[[string]$p.paragraph_id] = $true }
    $imageIds = @{}; foreach ($im in $images) { $imageIds[[string]$im.image_id] = $true }
    $evidenceIds = @{}; foreach ($e in @($r.evidence_refs)) { $evidenceIds[[string]$e.evidence_id] = $true; $paraRef=[string]$e.paragraph_id; $imageRef=[string]$e.image_id; if ($paraRef -and -not $paragraphIds.ContainsKey($paraRef)) { Fail("evidence paragraph missing $id/$paraRef") }; if ($imageRef -and -not $imageIds.ContainsKey($imageRef)) { Fail("evidence image missing $id/$imageRef") } }
    foreach ($claim in @($r.analysis.main_claims)) {
        $type=[string]$claim.claim_type; $refs=@($claim.evidence_refs)
        if ($type -in @('author_explicit','author_qualified','author_reported') -and $refs.Count -eq 0) { Fail("explicit claim without evidence $id/$($claim.claim_id)") }
        foreach ($ref in $refs) { if (-not $evidenceIds.ContainsKey([string]$ref)) { Fail("claim evidence ref missing $id/$ref") } }
    }
}
foreach ($in in $inputRows) { if (-not $outputIds.ContainsKey([string]$in.article.id)) { Fail("missing output for $($in.article.id)") } }
$result = [ordered]@{ status = if ($failures.Count -eq 0) { 'PASS' } else { 'FAIL' }; input_records = $inputRows.Count; output_records = $outputs.Count; failures = @($failures) }
$result | ConvertTo-Json -Depth 6
if ($failures.Count -gt 0) { exit 1 }
