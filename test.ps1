#!/usr/bin/env pwsh

function error([string] $msg) {
    Write-Host "[" -NoNewline
    Write-Host -ForegroundColor "Blue" "Ernaculere" -NoNewline
    Write-Host "]: " -NoNewline
    Write-Host "(" -NoNewline
    Write-Host -ForegroundColor "Red" "Error" -NoNewline
    Write-Host ": " -NoNewline
    Write-Host -ForegroundColor "DarkYellow" "bundle.ps1" -NoNewline
    Write-Host "): $msg"
}

function info([string] $msg) {
    Write-Host "[" -NoNewline
    Write-Host -ForegroundColor "Blue" "Ernaculere" -NoNewline
    Write-Host "]: " -NoNewline
    Write-Host "(" -NoNewline
    Write-Host -ForegroundColor "Green" "Info" -NoNewline
    Write-Host ": " -NoNewline
    Write-Host -ForegroundColor "DarkYellow" "bundle.ps1" -NoNewline
    Write-Host "): $msg"
}

if ($null -eq (Get-Command "deno.exe" -ErrorAction SilentlyContinue)) {
    error "Couldn't find 'deno.exe'"
    error "Please install 'deno.exe' and try again and set the PATH correctly"
    error "Aborting..."
    exit 1
}

deno test -qA .\test