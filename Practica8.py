# Practica 8 Envio de correos
# Mauricio Alejandro Torres Luna 1809779


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Creacion de un objeto de mensaje SMTP
msg = MIMEMultipart()

mensaje = input('Escribe el mesaje: ')

# Parametros del mensaje
password = input('Escribe tu contraseña: ')
msg['From'] = input('Escribe tu correo electronico: ')
msg['To'] = input('Escribe el correo electronico del destinatario: ')
msg['Subject'] = input('Descripción: ')

msg.attach(MIMEText(mensaje, 'plain'))

# Crear el Servidor
servidor = smtplib.SMTP('smtp.gmail.com', 587)
servidor.starttls()

# Ingresamos las credencial para envio del mensaje
servidor.login(msg['From'], password)

# Enviamos el mensaje con el servidor
servidor.sendmail(msg['From'], msg['To'], msg.as_string())
servidor.quit()

print('Mensaje Enviado correctamente a el correo', msg['To'])