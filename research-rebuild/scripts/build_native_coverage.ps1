#Requires -Version 7.0
<## Build an exact ID-based map between the official Sooon outline and the local corpus. ##>
[CmdletBinding()]
param(
    [string]$OutlinePath = (Join-Path $PSScriptRoot '..\data\sooon-official-outline.json'),
    [string]$RawPagesPath = (Join-Path $PSScriptRoot '..\data\native-raw\native-category-pages-20260921-225546.json'),
    [string]$CorpusPath = (Join-Path $PSScriptRoot '..\..\sooon-q9adg-articles-v2.jsonl'),
    [string]$OutputDir = (Join-Path $PSScriptRoot '..\reports\native-coverage')
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Write-JsonFile([object]$Value, [string]$Path) {
    $Value | ConvertTo-Json -Depth 50 | Set-Content -LiteralPath $Path -Encoding utf8NoBOM
}
function CsvValue([object]$Value) {
    if ($null -eq $Value) { return '' }
    return ([string]$Value).Replace('`r',' ').Replace('`n',' ')
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null
$outline = Get-Content -LiteralPath $OutlinePath -Raw | ConvertFrom-Json -Depth 50
$pages = Get-Content -LiteralPath $RawPagesPath -Raw | ConvertFrom-Json -Depth 50

# The outline is authoritative for the tree.  Raw pages are authoritative for
# which Source IDs were returned by each category, including pagination.
$categories = @($outline.categories)
$catById = @{}
foreach ($cat in $categories) { $catById[[string]$cat.id] = $cat }
$parentById = @{}
foreach ($cat in $categories) { $parentById[[string]$cat.id] = if ($cat.parentId) { [string]$cat.parentId } else { $null } }

$sourceCats = @{}
$pageStats = [System.Collections.Generic.List[object]]::new()
foreach ($page in $pages) {
    $catId = [string]$page.category.id
    $node = $page.response.data.leoCategorySourceList
    $items = @($node.items)
    $ids = [System.Collections.Generic.List[string]]::new()
    foreach ($item in $items) {
        $sourceId = [string]$item.id
        if ([string]::IsNullOrWhiteSpace($sourceId)) { continue }
        $ids.Add($sourceId)
        if (-not $sourceCats.ContainsKey($sourceId)) { $sourceCats[$sourceId] = [System.Collections.Generic.HashSet[string]]::new() }
        [void]$sourceCats[$sourceId].Add($catId)
    }
    $pageStats.Add([ordered]@{
        category_id = $catId
        category_name = [string]$page.category.name
        kind = [string]$page.category.kind
        item_count = $items.Count
        unique_item_count = @($ids | Sort-Object -Unique).Count
        next_cursor_present = [bool]$node.nextCursor
    })
}

$local = @{}
$localDuplicates = [System.Collections.Generic.List[object]]::new()
$localCount = 0
foreach ($line in [IO.File]::ReadLines((Resolve-Path -LiteralPath $CorpusPath))) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    $article = $line | ConvertFrom-Json -Depth 20
    $localCount++
    $id = [string]$article.id
    if ($local.ContainsKey($id)) {
        $localDuplicates.Add([ordered]@{ id = $id; first_title = [string]$local[$id].title; duplicate_title = [string]$article.title })
        continue
    }
    $local[$id] = [ordered]@{
        id = $id; title = [string]$article.title; question = [string]$article.question
        url = [string]$article.url; publishedAt = $article.publishedAt; updatedAt = $article.updatedAt
    }
}

$officialIds = [System.Collections.Generic.HashSet[string]]::new()
foreach ($id in $sourceCats.Keys) { [void]$officialIds.Add($id) }
$matchedIds = [System.Collections.Generic.HashSet[string]]::new()
foreach ($id in $officialIds) { if ($local.ContainsKey($id)) { [void]$matchedIds.Add($id) } }
$localWithoutOfficial = @($local.Keys | Where-Object { -not $officialIds.Contains([string]$_) })
$officialWithoutLocal = @($officialIds | Where-Object { -not $local.ContainsKey([string]$_) })

# Resolve a readable root-to-leaf path for every category.
$pathCache = @{}
function Get-CategoryPath([string]$Id) {
    if ($pathCache.ContainsKey($Id)) { return $pathCache[$Id] }
    $parts = [System.Collections.Generic.List[string]]::new()
    $seen = [System.Collections.Generic.HashSet[string]]::new()
    $cur = $Id
    while ($cur -and $catById.ContainsKey($cur) -and $seen.Add($cur)) {
        $parts.Insert(0, [string]$catById[$cur].name)
        $cur = $parentById[$cur]
    }
    $path = $parts -join ' / '
    $pathCache[$Id] = $path
    return $path
}

$categoryRows = [System.Collections.Generic.List[object]]::new()
foreach ($cat in $categories) {
    $catId = [string]$cat.id
    $catSourceIds = @($sourceCats.Keys | Where-Object { $sourceCats[$_].Contains($catId) })
    $matched = @($catSourceIds | Where-Object { $local.ContainsKey([string]$_) })
    $categoryRows.Add([ordered]@{
        category_id = $catId; name = [string]$cat.name; kind = [string]$cat.kind
        parent_id = if ($cat.parentId) { [string]$cat.parentId } else { '' }
        path = Get-CategoryPath $catId; description = [string]$cat.description
        official_source_count = $catSourceIds.Count; local_match_count = $matched.Count
        official_missing_local_count = $catSourceIds.Count - $matched.Count
        local_match_rate = if ($catSourceIds.Count) { [math]::Round($matched.Count / $catSourceIds.Count, 4) } else { 0 }
    })
}

$sourceRows = [System.Collections.Generic.List[object]]::new()
foreach ($id in ($sourceCats.Keys | Sort-Object)) {
    $catIds = @($sourceCats[$id] | Sort-Object)
    $names = @($catIds | ForEach-Object { [string]$catById[$_].name })
    $localArticle = if ($local.ContainsKey($id)) { $local[$id] } else { $null }
    $sourceRows.Add([ordered]@{
        source_id = $id; local_present = [bool]$localArticle; title = if ($localArticle) { $localArticle.title } else { '' }
        url = if ($localArticle) { $localArticle.url } else { '' }
        category_count = $catIds.Count; category_ids = ($catIds -join '|'); category_names = ($names -join '|')
        category_paths = (($catIds | ForEach-Object { Get-CategoryPath $_ }) -join '|')
    })
}

$unclassifiedRows = [System.Collections.Generic.List[object]]::new()
foreach ($id in ($localWithoutOfficial | Sort-Object)) {
    $a = $local[$id]
    $unclassifiedRows.Add([ordered]@{ id = $id; title = $a.title; question = $a.question; url = $a.url; publishedAt = $a.publishedAt; updatedAt = $a.updatedAt })
}
$multiRows = @($sourceRows | Where-Object { $_.category_count -gt 1 })
$pageItemTotal = 0
$pageUniqueItemTotal = 0
foreach ($p in $pageStats) {
    $pageItemTotal += [int]$p['item_count']
    $pageUniqueItemTotal += [int]$p['unique_item_count']
}

$categoryRows | Export-Csv -LiteralPath (Join-Path $OutputDir 'category-coverage.csv') -NoTypeInformation -Encoding utf8NoBOM
$sourceRows | Export-Csv -LiteralPath (Join-Path $OutputDir 'source-category-index.csv') -NoTypeInformation -Encoding utf8NoBOM
$unclassifiedRows | Export-Csv -LiteralPath (Join-Path $OutputDir 'local-unclassified.csv') -NoTypeInformation -Encoding utf8NoBOM
$multiRows | Export-Csv -LiteralPath (Join-Path $OutputDir 'multi-category-sources.csv') -NoTypeInformation -Encoding utf8NoBOM
$pageStats | Export-Csv -LiteralPath (Join-Path $OutputDir 'page-stats.csv') -NoTypeInformation -Encoding utf8NoBOM
$localDuplicates | Export-Csv -LiteralPath (Join-Path $OutputDir 'local-duplicate-ids.csv') -NoTypeInformation -Encoding utf8NoBOM

$tree = [ordered]@{
    generated_at = (Get-Date).ToString('o'); category_count = $categories.Count
    categories = @($categories | ForEach-Object {
        $id = [string]$_.id
        [ordered]@{ id = $id; name = [string]$_.name; description = [string]$_.description; kind = [string]$_.kind; parentId = if ($_.parentId) { [string]$_.parentId } else { $null }; path = Get-CategoryPath $id }
    })
}
Write-JsonFile $tree (Join-Path $OutputDir 'native-category-tree.json')

$coverage = [ordered]@{
    generated_at = (Get-Date).ToString('o'); corpus_path = (Resolve-Path -LiteralPath $CorpusPath).Path
    corpus_line_count = $localCount; local_unique_id_count = $local.Count; local_duplicate_id_count = $localDuplicates.Count
    official_category_count = $categories.Count; official_unique_source_id_count = $officialIds.Count
    official_source_ids_in_local = $matchedIds.Count; official_source_ids_missing_local = $officialWithoutLocal.Count
    local_ids_with_official_category = $matchedIds.Count; local_ids_without_official_category = $localWithoutOfficial.Count
    local_article_official_category_rate = if ($local.Count) { [math]::Round($matchedIds.Count / $local.Count, 6) } else { 0 }
    official_source_local_match_rate = if ($officialIds.Count) { [math]::Round($matchedIds.Count / $officialIds.Count, 6) } else { 0 }
    category_rows_with_zero_sources = @($categoryRows | Where-Object { $_.official_source_count -eq 0 }).Count
    category_rows_with_no_local_match = @($categoryRows | Where-Object { $_.official_source_count -gt 0 -and $_.local_match_count -eq 0 }).Count
    source_ids_in_multiple_categories = $multiRows.Count
    page_count = $pages.Count
    page_item_total = $pageItemTotal
    page_unique_item_total = $pageUniqueItemTotal
}
Write-JsonFile $coverage (Join-Path $OutputDir 'coverage-report.json')
$coverage | ConvertTo-Json -Depth 20
