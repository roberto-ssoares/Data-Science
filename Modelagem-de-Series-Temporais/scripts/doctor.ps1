param(
  [switch]$Fix
)

$ErrorActionPreference = "Stop"

function Ok($msg) { Write-Host "[OK]  $msg" -ForegroundColor Green }
function Warn($msg) { Write-Host "[WARN] $msg" -ForegroundColor Yellow }
function Fail($msg) { Write-Host "[FAIL] $msg" -ForegroundColor Red; exit 1 }

# 1) Local
$root = (Resolve-Path ".").Path
Ok "Project root: $root"

# 2) uv
$uv = Get-Command uv -ErrorAction SilentlyContinue
if (-not $uv) { Fail "uv não encontrado no PATH. Instale o uv e reabra o terminal." }
Ok "uv encontrado: $($uv.Source)"

# 3) .python-version
if (-not (Test-Path ".python-version")) { Warn ".python-version não existe (recomendado criar)." }
else {
  $pyver = (Get-Content ".python-version" -Raw).Trim()
  Ok ".python-version = $pyver"
}

# 4) venv
if (-not (Test-Path ".venv")) {
  Warn ".venv não existe."
  if ($Fix) {
    Ok "Criando .venv via uv venv..."
    uv venv | Out-Host
  } else {
    Warn "Rode: uv venv"
  }
} else {
  Ok ".venv existe"
}

# 5) sync deps
Ok "Rodando uv sync..."
if (Test-Path "tests") {
  Ok "Rodando uv sync (com extra dev)..."
  uv sync --extra dev | Out-Host
  if ($LASTEXITCODE -ne 0) { Fail "uv sync falhou" }
} else {
  Ok "Rodando uv sync..."
  uv sync | Out-Host
  if ($LASTEXITCODE -ne 0) { Fail "uv sync falhou" }
}
Ok "uv sync concluído"

# 6) sanity imports
Ok "Testando imports (numpy/pandas/statsmodels)..."
uv run python -c "import numpy, pandas, statsmodels; print('imports ok')"
if ($LASTEXITCODE -ne 0) { Fail "imports falharam" }
Ok "Imports OK"

# 7) pytest (se existir)
if (Test-Path "tests") {
  Ok "Rodando pytest..."
  uv run pytest
  if ($LASTEXITCODE -ne 0) { Fail "pytest falhou" }
  Ok "pytest OK"
} else {
  Warn "Pasta tests/ não encontrada (opcional)."
}

Ok "Doctor finalizado ✅"
