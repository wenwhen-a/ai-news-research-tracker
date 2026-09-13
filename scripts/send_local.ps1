# Send a folder of digest messages to Discord from this PC.
# Usage:
#   powershell -ExecutionPolicy Bypass -File "<repo>\scripts\send_local.ps1" -Dir "digests\2026-09-13\messages"
# Asks for the webhook URL (typed hidden), dry-runs first, then posts every *.md in the folder in sorted order.
# The URL lives only inside this process and is cleared at the end.

param(
    [Parameter(Mandatory = $true)] [string] $Dir
)

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo
$target = if ([System.IO.Path]::IsPathRooted($Dir)) { $Dir } else { Join-Path $repo $Dir }
if (-not (Test-Path $target -PathType Container)) { throw "Messages folder not found: $target" }
Write-Host "Repo:     $repo"
Write-Host "Messages: $target"

Write-Host "`n== Dry run ==" -ForegroundColor Cyan
python scripts/send_discord.py --dir $target --dry-run
if ($LASTEXITCODE -ne 0) { throw "Dry run failed with exit code $LASTEXITCODE (2 = a message is over 2000 chars; fix it and re-run)" }

$secure = Read-Host -Prompt "Paste the Discord webhook URL (input hidden)" -AsSecureString
$bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
try {
    $env:DISCORD_WEBHOOK_URL = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr).Trim()
} finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
}
if (-not $env:DISCORD_WEBHOOK_URL.StartsWith("https://discord.com/api/webhooks/") -and
    -not $env:DISCORD_WEBHOOK_URL.StartsWith("https://discordapp.com/api/webhooks/")) {
    $env:DISCORD_WEBHOOK_URL = $null
    throw "That does not look like a Discord webhook URL (expected https://discord.com/api/webhooks/...)."
}

Write-Host "`n== Sending ==" -ForegroundColor Cyan
python scripts/send_discord.py --dir $target
$code = $LASTEXITCODE
$env:DISCORD_WEBHOOK_URL = $null

if ($code -eq 0) {
    Write-Host "`nOK - all messages posted. Check the Discord channel." -ForegroundColor Green
} else {
    Write-Host "`nSend failed with exit code $code (1 = Discord rejected a message, 2 = message too long, 3 = URL missing)." -ForegroundColor Red
}
exit $code
