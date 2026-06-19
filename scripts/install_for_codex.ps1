param(
    [ValidateSet("repo", "user")]
    [string]$Scope = "repo",
    [string]$TargetPath = (Get-Location).Path,
    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$sourceRoot = Join-Path $repoRoot "skills"
$supportFolders = @("agents", "workflows", "rules", "scripts")
$skillNames = @("odoo-development", "odoo-14.0", "odoo-15.0", "odoo-16.0", "odoo-17.0", "odoo-18.0", "odoo-19.0")

if ($Scope -eq "user") {
    $codexRoot = Join-Path $HOME ".agents"
} else {
    $codexRoot = Join-Path (Resolve-Path $TargetPath).Path ".agents"
}

$destinationRoot = Join-Path $codexRoot "skills"
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
    Write-Output "Codex skill installed to: $destination"
}

foreach ($folderName in $supportFolders) {
    $sourceFolder = Join-Path $repoRoot $folderName
    if (-not (Test-Path $sourceFolder)) {
        throw "Support folder not found: $sourceFolder"
    }

    $destinationFolder = Join-Path $codexRoot $folderName
    if ((Test-Path $destinationFolder) -and -not $Force) {
        throw "Destination already exists: $destinationFolder. Re-run with -Force to overwrite."
    }

    if (Test-Path $destinationFolder) {
        Remove-Item -Recurse -Force -LiteralPath $destinationFolder
    }

    Copy-Item -Recurse -Force -LiteralPath $sourceFolder -Destination $destinationFolder
    Write-Output "Codex support folder installed to: $destinationFolder"
}
