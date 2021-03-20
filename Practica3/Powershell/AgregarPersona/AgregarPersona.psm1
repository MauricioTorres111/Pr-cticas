function AgregarPersona{
$Key = Read-Host -Prompt "Coloca el ID del equipo al que deseas agregar " 
$Persona = Read-Host -Prompt "Coloca el correo de la persona que deseas agregar " 
Add-TeamUser -GroupId $Key -User $Persona -Role Member
}