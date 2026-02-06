# Script para crear tarea automatica en Windows Task Scheduler
# Ejecuta el organizador de descargas todos los domingos a las 20:00
# IMPORTANTE: Ejecutar como Administrador

$TaskName = "OrganizarDescargas"
$ScriptPath = "$PSScriptRoot\script_descargas.py"
$PythonPath = "$PSScriptRoot\..\.venv\Scripts\python.exe"

# Verificar si se esta ejecutando como administrador
$isAdmin = ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERROR: Este script debe ejecutarse como Administrador" -ForegroundColor Red
    Write-Host ""
    Write-Host "Pasos:" -ForegroundColor Yellow
    Write-Host "1. Cierra esta ventana" -ForegroundColor Cyan
    Write-Host "2. Abre PowerShell como Administrador (Win + X -> PowerShell Admin)" -ForegroundColor Cyan
    Write-Host "3. Navega a: cd C:\Users\cerra\codigo\Scripts\src" -ForegroundColor Cyan
    Write-Host "4. Ejecuta: .\crear_tarea_automatica.ps1" -ForegroundColor Cyan
    Write-Host ""
    pause
    exit 1
}

# Verificar que existe el Python del entorno virtual
if (-not (Test-Path $PythonPath)) {
    Write-Host "Error: No se encuentra Python en $PythonPath" -ForegroundColor Red
    Write-Host "Asegurate de que el entorno virtual este creado en .venv" -ForegroundColor Yellow
    exit 1
}

# Verificar que existe el script
if (-not (Test-Path $ScriptPath)) {
    Write-Host "Error: No se encuentra el script en $ScriptPath" -ForegroundColor Red
    exit 1
}

# Crear la accion (ejecutar Python con el script)
$Action = New-ScheduledTaskAction -Execute $PythonPath -Argument "`"$ScriptPath`""

# Crear el trigger (todos los domingos a las 20:00)
$Trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 20:00

# Configuracion adicional
$Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

# Descripcion de la tarea
$Description = "Organiza automaticamente los archivos de la carpeta Descargas cada domingo a las 20:00"

# Registrar la tarea
try {
    Register-ScheduledTask -TaskName $TaskName -Action $Action -Trigger $Trigger -Settings $Settings -Description $Description -Force
    Write-Host "Tarea '$TaskName' creada exitosamente" -ForegroundColor Green
    Write-Host "Se ejecutara todos los domingos a las 20:00" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Para ver la tarea: taskschd.msc" -ForegroundColor Yellow
    Write-Host "Para probar ahora: schtasks /run /tn `"$TaskName`"" -ForegroundColor Yellow
} catch {
    $ErrorMsg = $_.Exception.Message
    Write-Host "Error al crear la tarea: $ErrorMsg" -ForegroundColor Red
    exit 1
}
