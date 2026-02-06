# Script para eliminar la tarea automatica del Task Scheduler

$TaskName = "OrganizarDescargas"

try {
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
    Write-Host "Tarea '$TaskName' eliminada exitosamente" -ForegroundColor Green
} catch {
    $ErrorMsg = $_.Exception.Message
    Write-Host "Error: No se pudo eliminar la tarea. Puede que no exista." -ForegroundColor Red
    Write-Host "Detalles: $ErrorMsg" -ForegroundColor Red
}
