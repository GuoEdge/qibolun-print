$ErrorActionPreference = 'Stop'

$root = (Get-Location).Path
$corpusPath = Join-Path $root 'sooon-q9adg-articles-v2.jsonl'
$inventoryPath = Join-Path $root 'research-rebuild/data/image-inventory.csv'
$decisionPath = Join-Path $root 'research-rebuild/data/print-topic-manual-decisions-v2.csv'
$queuePath = Join-Path $root 'research-rebuild/reports/live-manual-classification-queue-v2.csv'
$reportDir = Join-Path $root 'research-rebuild/reports'
$outCsv = Join-Path $reportDir 'image-article-inventory-audit-v1.csv'
$outSummary = Join-Path $reportDir 'image-article-inventory-audit-v1.summary.json'

$articles = @(Get-Content -LiteralPath $corpusPath -Encoding utf8 | ForEach-Object { $_ | ConvertFrom-Json })
$inventory = @(Import-Csv -LiteralPath $inventoryPath -Encoding utf8)
$decisions = @(Import-Csv -LiteralPath $decisionPath -Encoding utf8)
$queue = @(Import-Csv -LiteralPath $queuePath -Encoding utf8)
$reviewFiles = @(Get-ChildItem $reportDir -File | Where-Object { $_.Name -match '^round(114|115|116|117|118|119|120|121|122|123|136|140|141)-image-review\.tsv$' })
$reviews = @()
foreach ($file in $reviewFiles) {
    $reviews += @(Import-Csv -LiteralPath $file.FullName -Delimiter "`t" -Encoding utf8)
}

$inventoryById = @{}
foreach ($row in $inventory) {
    if (-not $inventoryById.ContainsKey($row.id)) { $inventoryById[$row.id] = @() }
    $inventoryById[$row.id] += $row
}
$reviewById = @{}
foreach ($row in $reviews) {
    if (-not $reviewById.ContainsKey($row.id)) { $reviewById[$row.id] = @() }
    $reviewById[$row.id] += $row
}
$decisionById = @{}
foreach ($row in $decisions) { $decisionById[$row.id] = $row }
$queueById = @{}
foreach ($row in $queue) { $queueById[$row.id] = $row }

# These phrases indicate that the image is contextual, weakly related, or not evidence.
$weakPattern = '关系弱|关系有限|对应关系不清|对应关系弱|仅能确认|只能确认|仅支持|仅对应|仅提供|只能表现|仅作空白|无法建立可靠对应|不能作为|不直接|附图语境|弱关联|关联有限|主题关系弱|主体.*不清|未见可识别'

$rows = foreach ($article in $articles) {
    $text = [string]$article.text
    $lexical = [string]$article.lexical
    $imageCount = ([regex]::Matches($lexical, '"type":"image"')).Count
    if ($imageCount -eq 0) { continue }

    $inventoryRows = if ($inventoryById.ContainsKey($article.id)) { @($inventoryById[$article.id]) } else { @() }
    $reviewRows = if ($reviewById.ContainsKey($article.id)) { @($reviewById[$article.id]) } else { @() }
    $decision = if ($decisionById.ContainsKey($article.id)) { $decisionById[$article.id] } else { $null }
    $queueRow = if ($queueById.ContainsKey($article.id)) { $queueById[$article.id] } else { $null }
    $reviewedImages = @($inventoryRows | Where-Object { $_.status -eq 'reviewed' }).Count
    $unreviewedImages = @($inventoryRows | Where-Object { $_.status -ne 'reviewed' }).Count
    $reviewState = if ($reviewedImages -eq 0) { 'none_reviewed' } elseif ($reviewedImages -eq $inventoryRows.Count) { 'all_reviewed' } else { 'partial' }
    $weakRows = @($reviewRows | Where-Object { ([string]$_.relation_to_text) -match $weakPattern })
    $consistency = @($reviewRows | ForEach-Object { [string]$_.image_text_consistency } | Where-Object { $_ })
    $weakCount = $weakRows.Count
    $imageRole = if ($reviewedImages -eq 0) { 'unreviewed' } elseif ($weakCount -gt 0) { 'reviewed_weak_or_mixed' } elseif ($consistency -contains 'consistent') { 'reviewed_supports_or_direct' } else { 'reviewed_limited' }
    $chars = $text.Length
    $band = if ($chars -eq 0) { '0' } elseif ($chars -le 50) { '1-50' } elseif ($chars -le 200) { '51-200' } elseif ($chars -le 500) { '201-500' } elseif ($chars -le 1000) { '501-1000' } else { '>1000' }
    $sufficiency = if ($chars -eq 0) { 'none' } elseif ($chars -le 50) { 'micro' } elseif ($chars -le 200) { 'short' } elseif ($chars -le 500) { 'moderate' } elseif ($chars -le 1000) { 'substantial' } else { 'full' }

    # Candidate action is deliberately conservative and does not alter the corpus.
    $candidate = if ($chars -eq 0) {
        'discard_article_candidate_image_only_no_text'
    } elseif ($chars -le 50) {
        'micro_body_manual_decision'
    } elseif ($chars -le 200 -and $unreviewedImages -gt 0) {
        'short_body_image_review_pending'
    } elseif ($chars -le 200 -and $weakCount -gt 0) {
        'short_body_keep_text_drop_weak_images_candidate'
    } elseif ($chars -le 200) {
        'short_body_keep_with_images_or_manual_check'
    } elseif ($unreviewedImages -gt 0) {
        'retain_article_image_review_pending'
    } elseif ($weakCount -gt 0) {
        'retain_article_drop_weak_or_decorative_images_candidate'
    } else {
        'retain_article_images_optional'
    }

    [pscustomobject]@{
        id = $article.id
        title = [string]$article.title
        question = [string]$article.question
        url = [string]$article.url
        text_chars = $chars
        text_length_band = $band
        body_sufficiency = $sufficiency
        image_count = $imageCount
        inventory_image_count = $inventoryRows.Count
        image_count_mismatch = ($imageCount -ne $inventoryRows.Count)
        image_review_state = $reviewState
        reviewed_images = $reviewedImages
        unreviewed_images = $unreviewedImages
        reviewed_consistency = (($consistency | Sort-Object -Unique) -join ';')
        weak_or_unclear_relation_count = $weakCount
        image_role = $imageRole
        candidate_disposition = $candidate
        formal_primary_topic = if ($decision) { $decision.primary_print_topic_code } else { '' }
        formal_status = if ($decision) { $decision.classification_status } else { '' }
        queue_priority = if ($queueRow) { $queueRow.priority } else { '' }
        queue_reasons = if ($queueRow) { $queueRow.reasons } else { '' }
        weak_relation_samples = (@($weakRows | Select-Object -First 3 -ExpandProperty relation_to_text) -join ' || ')
    }
}

$rows = @($rows | Sort-Object text_chars, id)
$utf8NoBom = New-Object System.Text.UTF8Encoding($false)
$csv = (($rows | ConvertTo-Csv -NoTypeInformation) -join [Environment]::NewLine) + [Environment]::NewLine
[IO.File]::WriteAllText($outCsv, $csv, $utf8NoBom)

$summary = [ordered]@{
    generated_at = (Get-Date).ToString('o')
    corpus_path = $corpusPath
    corpus_records = $articles.Count
    image_article_count = $rows.Count
    image_node_count = [int](($rows | Measure-Object image_count -Sum).Sum)
    inventory_rows = $inventory.Count
    image_count_mismatch_articles = @($rows | Where-Object image_count_mismatch).Count
    reviewed_image_nodes = [int](($rows | Measure-Object reviewed_images -Sum).Sum)
    unreviewed_image_nodes = [int](($rows | Measure-Object unreviewed_images -Sum).Sum)
    all_images_reviewed_articles = @($rows | Where-Object image_review_state -eq 'all_reviewed').Count
    no_images_reviewed_articles = @($rows | Where-Object image_review_state -eq 'none_reviewed').Count
    partial_images_reviewed_articles = @($rows | Where-Object image_review_state -eq 'partial').Count
    text_length_bands = [ordered]@{}
    image_role_counts = [ordered]@{}
    candidate_disposition_counts = [ordered]@{}
    weak_or_unclear_relation_articles = @($rows | Where-Object weak_or_unclear_relation_count -gt 0).Count
    zero_text_articles = @($rows | Where-Object text_chars -eq 0 | Select-Object id,title,question,image_count,image_review_state,candidate_disposition)
    micro_text_articles = @($rows | Where-Object { $_.text_chars -gt 0 -and $_.text_chars -le 50 } | Select-Object id,title,question,text_chars,image_count,image_review_state,candidate_disposition)
    short_text_articles = @($rows | Where-Object { $_.text_chars -gt 50 -and $_.text_chars -le 200 } | Select-Object id,title,question,text_chars,image_count,image_review_state,candidate_disposition)
    weak_relation_samples = @($rows | Where-Object weak_or_unclear_relation_count -gt 0 | Select-Object -First 30 id,title,text_chars,image_count,image_role,weak_or_unclear_relation_count,weak_relation_samples)
}
foreach ($band in @('0','1-50','51-200','201-500','501-1000','>1000')) { $summary.text_length_bands[$band] = @($rows | Where-Object text_length_band -eq $band).Count }
foreach ($role in @('unreviewed','reviewed_weak_or_mixed','reviewed_supports_or_direct','reviewed_limited')) { $summary.image_role_counts[$role] = @($rows | Where-Object image_role -eq $role).Count }
foreach ($candidate in @('discard_article_candidate_image_only_no_text','micro_body_manual_decision','short_body_image_review_pending','short_body_keep_text_drop_weak_images_candidate','short_body_keep_with_images_or_manual_check','retain_article_image_review_pending','retain_article_drop_weak_or_decorative_images_candidate','retain_article_images_optional')) { $summary.candidate_disposition_counts[$candidate] = @($rows | Where-Object candidate_disposition -eq $candidate).Count }
[IO.File]::WriteAllText($outSummary, ($summary | ConvertTo-Json -Depth 12), $utf8NoBom)

Write-Output "CSV=$outCsv"
Write-Output "SUMMARY=$outSummary"
Write-Output "ROWS=$($rows.Count)"
Write-Output "IMAGE_NODES=$([int](($rows | Measure-Object image_count -Sum).Sum))"
Write-Output "REVIEWED_NODES=$([int](($rows | Measure-Object reviewed_images -Sum).Sum))"
Write-Output "UNREVIEWED_NODES=$([int](($rows | Measure-Object unreviewed_images -Sum).Sum))"
