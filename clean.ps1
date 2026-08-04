# ============================================================
# GS1 Scanner - Clean Script
# ============================================================

$Root = Split-Path `
    -Parent `
    (Split-Path `
        -Parent `
        $MyInvocation.MyCommand.Path
    )


Set-Location $Root


$Targets = @(
    "build",
    "dist",
    "__pycache__"
)


foreach($item in $Targets){

    if(Test-Path $item){

        Write-Host "Removing $item..."

        Remove-Item `
            $item `
            -Recurse `
            -Force
    }
}


Get-ChildItem `
    -Recurse `
    -Directory `
    -Filter "__pycache__" |
    Remove-Item `
    -Recurse `
    -Force


Write-Host ""
Write-Host "Clean completed."