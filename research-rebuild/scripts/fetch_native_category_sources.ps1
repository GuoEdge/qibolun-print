#Requires -Version 7.0
<## Fetch articles assigned to the official Leo categories via persisted GraphQL. ##>
param(
    [string]$CurlFile = (Join-Path $PSScriptRoot '..\..\research\online-increment\.session-curl'),
    [string]$OutlinePath = (Join-Path $PSScriptRoot '..\data\sooon-official-outline.json'),
    [string]$OutputDir = (Join-Path $PSScriptRoot '..\data\native-raw'),
    [switch]$ProbeOnly,
    [int]$PageSize = 100
)
$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Read-CurlValue([string]$Text, [string]$Name, [switch]$Cookie) {
    $pattern = if ($Cookie) { '(?is)(?:(?:-b|--cookie)\s+|(?:-H|--header)\s+[''\"]?cookie:\s*)[''\"]?(?<v>[^''\"\r\n]+)[''\"]?' } else { '(?is)(?:-H|--header)\s+[''\"]?' + [regex]::Escape($Name) + ':\s*(?<v>[^''\"\r\n]+)' }
    $m = [regex]::Match($Text, $pattern)
    if (-not $m.Success) { throw "未找到 $Name" }
    return $m.Groups['v'].Value.Trim()
}

$curlText = Get-Content -LiteralPath $CurlFile -Raw
$cookie = Read-CurlValue $curlText 'cookie' -Cookie
$csrf = Read-CurlValue $curlText 'x-graphql-csrf'
$outline = Get-Content -LiteralPath $OutlinePath -Raw | ConvertFrom-Json -Depth 20
$graphId = [string]$outline.graphs[0].officialGraph.id
$queryHash = 'sha256:7b0dfd92fa6399bd1d9b8fa957ceb6b17a495d9e2041de89d30e9c2d84b80457'
if (-not (Test-Path -LiteralPath $OutputDir)) { New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null }

function Invoke-CategoryPage([string]$CategoryId, [string]$After) {
    $payload = [ordered]@{
        operationName = 'LeoCategorySourceList'
        variables = @{ input = @{ graphId = $graphId; categoryId = $CategoryId; after = $After } }
        extensions = @{ persistedQuery = @{ version = 1; sha256Hash = $queryHash } }
    }
    $bodyPath = Join-Path ([IO.Path]::GetTempPath()) ("sooon-cat-body-{0}.json" -f [guid]::NewGuid().ToString('N'))
    $outPath = Join-Path ([IO.Path]::GetTempPath()) ("sooon-cat-out-{0}.json" -f [guid]::NewGuid().ToString('N'))
    $payload | ConvertTo-Json -Depth 20 -Compress | Set-Content -LiteralPath $bodyPath -Encoding utf8NoBOM
    try {
        $b = $bodyPath -replace '\\','/'
        $o = $outPath -replace '\\','/'
        $lines = @(
            'url = "https://sooon.ai/api/graphql"','request = "POST"','silent','show-error','max-time = 45','connect-timeout = 15','retry = 2','retry-delay = 2','retry-all-errors',
            'header = "content-type: application/json"','header = "accept: application/json"',"header = `"x-graphql-csrf: $csrf`"",'header = "origin: https://sooon.ai"','header = "referer: https://sooon.ai/"',"header = `"cookie: $cookie`"","data-binary = `"@$b`"","output = `"$o`"",'write-out = "%{http_code}"'
        )
        $status = (($lines -join "`n") | & curl.exe -K - 2>&1 | Out-String).Trim()
        if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath $outPath)) { throw "curl failed: $status" }
        $raw = [IO.File]::ReadAllText($outPath,[Text.UTF8Encoding]::new($false))
        $json = $raw | ConvertFrom-Json -Depth 40
        if ($json.PSObject.Properties.Name -contains 'errors' -and $json.errors) { throw (($json.errors | ForEach-Object {[string]$_.message}) -join ' | ') }
        return $json
    } finally {
        Remove-Item -LiteralPath $bodyPath,$outPath -Force -ErrorAction SilentlyContinue
    }
}

$categories = @($outline.categories)
$target = $categories | Where-Object { $_.kind -eq 'LeoPractice' } | Select-Object -First 1
if (-not $target) { $target = $categories | Select-Object -First 1 }
$probe = Invoke-CategoryPage ([string]$target.id) $null
if ($ProbeOnly) {
    $probe | ConvertTo-Json -Depth 40 | Write-Output
    exit 0
}

$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$all = [System.Collections.Generic.List[object]]::new()
foreach ($cat in $categories) {
    $after = $null
    do {
        $page = Invoke-CategoryPage ([string]$cat.id) $after
        $all.Add([ordered]@{ category = $cat; response = $page })
        $node = $page.data.leoCategorySourceList
        $after = if ($node.nextCursor) { [string]$node.nextCursor } else { $null }
    } while ($after)
}
$out = Join-Path $OutputDir "native-category-pages-$stamp.json"
$all | ConvertTo-Json -Depth 50 | Set-Content -LiteralPath $out -Encoding utf8NoBOM
[ordered]@{ output = $out; pages = $all.Count; categories = $categories.Count } | ConvertTo-Json
