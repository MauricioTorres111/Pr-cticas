function EliminarEquipo{
$ID = Read-Host -Prompt "Escribe el ID del equipo que quieres eliminar" 
Remove-Team -GroupId $ID
}