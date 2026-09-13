# Local one-off test of the Discord webhook sender.
# Run from anywhere:  powershell -ExecutionPolicy Bypass -File "C:\Users\ruoyu\OneDrive\Desktop\AI News and Research Paper\scripts\test_discord.ps1"
# It asks for the webhook URL (typed hidden), posts one test message, and forgets the URL when it exits.

$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
Set-Location $repo
Write-Host "Repo: $repo"

# 1. Dry run on a throwaway message file (no network)
$testFile = Join-Path $repo "test_message.md"
$stamp = Get-Date -Format "yyyy-MM-dd HH:mm"
"**Research Tracker test** - posted from $env:COMPUTERNAME at $stamp. If you can read this, the webhook works." | Out-File -FilePath $testFile -Encoding utf8

Write-Host "`n== Dry run ==" -ForegroundColor Cyan
python scripts/send_discord.py --file $testFile --dry-run
if ($LASTEXITCODE -ne 0) { Remove-Item $testFile; throw "Dry run failed with exit code $LASTEXITCODE" }

# 2. Ask for the webhook URL (hidden input), keep it only in this process
$secure = Read-Host -Prompt "Paste the Discord webhook URL (input hidden)" -AsSecureString
$bstr = [Runtime.InteropServices.Marshal]::SecureStringToBSTR($secure)
try {
    $env:DISCORD_WEBHOOK_URL = [Runtime.InteropServices.Marshal]::PtrToStringBSTR($bstr).Trim()
} finally {
    [Runtime.InteropServices.Marshal]::ZeroFreeBSTR($bstr)
}
if (-not $env:DISCORD_WEBHOOK_URL.StartsWith("https://discord.com/api/webhooks/") -and
    -not $env:DISCORD_WEBHOOK_URL.StartsWith("https://discordapp.com/api/webhooks/")) {
    Remove-Item $testFile
    $env:DISCORD_WEBHOOK_URL = $null
    throw "That does not look like a Discord webhook URL (expected https://discord.com/api/webhooks/...)."
}

# 3. Real send
Write-Host "`n== Sending ==" -ForegroundColor Cyan
python scripts/send_discord.py --file $testFile
$code = $LASTEXITCODE

# 4. Clean up: remove the test file and drop the secret from this session
Remove-Item $testFile
$env:DISCORD_WEBHOOK_URL = $null

if ($code -eq 0) {
    Write-Host "`nOK - check the Discord channel for the test message." -ForegroundColor Green
} else {
    Write-Host "`nSend failed with exit code $code (1 = Discord rejected it, 2 = message too long, 3 = URL missing)." -ForegroundColor Red
}
exit $code
