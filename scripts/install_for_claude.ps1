param(
    [ValidateSet("project", "user")]
    [string]$Scope = "project",
    [string]$TargetPath = (Get-Location).Path,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $repoRoot "skills"
$skillNames = @("odoo-development", "odoo-14.0", "odoo-15.0", "odoo-16.0", "odoo-17.0", "odoo-18.0", "odoo-19.0")
$supportFolders = @("agents", "workflows", "rules", "scripts")

if ($Scope -eq "user") {
    $hostRoot = Join-Path $HOME ".claude"
} else {
    $hostRoot = Join-Path (Resolve-Path $TargetPath).Path ".claude"
}

$destinationRoot = Join-Path $hostRoot "skills"
New-Item -ItemType Directory -Force -Path $destinationRoot | Out-Null
foreach ($skillName in $skillNames) {
    $sourceSkill = Join-Path $sourceRoot $skillName
    if (-not (Test-Path $sourceSkill)) {
        throw "Source skill not found: $sourceSkill"
    }

    $destination = Join-Path $destinationRoot $skillName
    if ((Test-Path $destination) -and -not $Force) {
        throw "Destination already exists: $destination. Re-run with -Force to overwrite."
    }

    if (Test-Path $destination) {
        Remove-Item -Recurse -Force -LiteralPath $destination
    }

    Copy-Item -Recurse -Force -LiteralPath $sourceSkill -Destination $destination
    Write-Output "Claude skill installed to: $destination"
}

foreach ($folderName in $supportFolders) {
    $sourceFolder = Join-Path $repoRoot $folderName
    if (-not (Test-Path $sourceFolder)) {
        throw "Support folder not found: $sourceFolder"
    }

    $destinationFolder = Join-Path $hostRoot $folderName
    if (Test-Path $destinationFolder) {
        if (-not $Force) {
            throw "Destination already exists: $destinationFolder. Re-run with -Force to overwrite."
        }
        Remove-Item -Recurse -Force -LiteralPath $destinationFolder
    }

    Copy-Item -Recurse -Force -LiteralPath $sourceFolder -Destination $destinationFolder
    Write-Output "Claude support folder installed to: $destinationFolder"
}
