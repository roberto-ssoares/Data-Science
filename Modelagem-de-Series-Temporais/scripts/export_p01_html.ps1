$ErrorActionPreference = "Stop"

$P01 = "projects/P01-time-series-active-users-forecast"
$NB  = Join-Path $P01 "notebooks"
$OUT = Join-Path $P01 "reports/exports"

New-Item -ItemType Directory -Force -Path $OUT | Out-Null

# Exporta todos os notebooks P01-*.ipynb
Get-ChildItem $NB -Filter "P01-*.ipynb" | ForEach-Object {
  $in = $_.FullName
  $name = $_.BaseName
  $out = Join-Path $OUT "$name.html"

  Write-Host "Exportando: $($_.Name) -> $out"
  uv run jupyter nbconvert --to html --execute --output $out $in
}

Write-Host "OK: exports em $OUT"






# .\scripts\export_p01_html.ps1

