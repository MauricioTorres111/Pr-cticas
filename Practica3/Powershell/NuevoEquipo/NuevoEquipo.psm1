function NuevoEquipo {
    $Eq = Read-Host -Prompt "Pon un nombre para tu nuevo equipo"
    New-Team -DisplayName $Eq 
}