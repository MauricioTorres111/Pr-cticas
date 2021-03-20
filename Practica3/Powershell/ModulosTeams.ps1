Import-Module VerEquipo
Import-Module NuevoEquipo
Import-Module EliminarEquipo
Import-Module AgregarPersona
Import-Module CambiarImagen

Write-Host "Porfavor digita tus credenciales"
$Datos = Get-Credential
Connect-MicrosoftTeams -Credential $Datos

function Menu-Selec{
    $Op = Read-Host -Prompt "
      [1] Ver Equipos
      [2] Crear Equipo
      [3] Eliminar Equipo
      [4] Agregar Usuario
      [5] Cambiar Imagen
      [6] Salir del Programa
       Ingresa una Opcion  "
    
    switch ($Op){
        1{VerEquipo}
        2{NuevoEquipo}
        3{EliminarEquipo}
        4{AgregarPersona}
        5{CambiarImagen}
        6{clear
          Write-Host "`n`Saliendo del programa...`n` "
          Exit }
        Default {Write-Host "`n` No conozco ese numero"}
    }}

do
{
 
Menu-Selec

}while($true)