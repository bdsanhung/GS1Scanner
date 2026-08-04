# ============================================================
# GS1 Scanner - Run Development
# ============================================================


$Root = Split-Path `
    -Parent `
    (Split-Path `
        -Parent `
        $MyInvocation.MyCommand.Path
    )



Set-Location $Root



Write-Host "===================================="
Write-Host " Starting GS1 Scanner"
Write-Host "===================================="



# Create venv if missing

if (!(Test-Path ".\.venv")) {


    Write-Host "Creating virtual environment..."


    python -m venv .venv

}





# Activate venv

& ".\.venv\Scripts\Activate.ps1"





# Install dependency

pip install -r requirements.txt





# Run

python main.py