param(
    [Parameter(Position=0)]
    [string]$Task
)

$BASE_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $BASE_DIR

function Install {
    Write-Host "📦 Installing dependencies..." -ForegroundColor Cyan
    uv pip install -r app/requirements.txt
}

function Prepare {
    Write-Host "⚙ Preparing data..." -ForegroundColor Yellow
    python scripts/prepare_data.py
}

function Run {
    Write-Host "🚀 Starting Streamlit app..." -ForegroundColor Green
    python scripts/run_app.py
}

function Help {
    Write-Host ""
    Write-Host "Available commands:" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "  .\tasks install    -> install dependencies"
    Write-Host "  .\tasks prepare    -> run data pipeline"
    Write-Host "  .\tasks run        -> start Streamlit app"
    Write-Host ""
}

switch ($Task) {
    "install" { Install }
    "prepare" { Prepare }
    "run" { Run }
    default { Help }
}