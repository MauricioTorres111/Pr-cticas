# Practica 7 Obtener Archivos con FTP
# Mauricio Alejandro Torres Luna

import ftplib

def Cliente_Conexion(Servidor, Name, email):
    ftp = ftplib.FTP(Servidor, Name, email)
    #Se listaran los archivos encontrados en el directorio
    ftp.cwd('/pub')
    print('Archivos disponibles en el servidor ', Servidor )
    archivos = ftp.dir()
    print(archivos)
    ftp.quit()

Ruta_Servidor_FTP = 'ftp.kernel.org'

if __name__ == '__main__':
    Cliente_Conexion(Servidor=Ruta_Servidor_FTP, Name='anonymous', Email='nobody@nourl.com')