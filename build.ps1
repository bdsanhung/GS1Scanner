# ============================================================
# GS1 Scanner - Build EXE
# PyInstaller
# ============================================================


$Root = Split-Path `
    -Parent `
    $MyInvocation.MyCommand.Path


Set-Location $Root



Write-Host "===================================="
Write-Host " GS1 Scanner Build"
Write-Host "===================================="



# Check venv

if (!(Test-Path ".\.venv")) {


    Write-Host "Creating virtual environment..."


    python -m venv .venv

}



# Activate

& ".\.venv\Scripts\Activate.ps1"



Write-Host "Updating packages..."


python -m pip install --upgrade pip



pip install -r requirements.txt





# Clean

if (Test-Path ".\build") {

    Remove-Item `
        ".\build" `
        -Recurse `
        -Force

}



if (Test-Path ".\dist") {

    Remove-Item `
        ".\dist" `
        -Recurse `
        -Force

}





Write-Host "Building..."



pyinstaller `

    --name GS1Scanner `

    --windowed `

    --onedir `

    --clean `

    --noconfirm `

    --add-data "app\resources;app\resources" `

    --add-data "app\data;app\data" `

    --add-data "app\styles;app\styles" `

    main.py





Write-Host ""

Write-Host "===================================="

Write-Host " BUILD SUCCESS"

Write-Host " Output:"

Write-Host " dist\GS1Scanner"

Write-Host "===================================="