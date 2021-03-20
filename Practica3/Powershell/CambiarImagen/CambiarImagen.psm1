function CambiarImagen{
$Equipo = Read-Host "Coloca el ID del grupo "
$Ruta = Read-Host "Coloca la direccion de la imagen "
Set-TeamPicture -GroupId $Equipo -ImagePath $Ruta
}