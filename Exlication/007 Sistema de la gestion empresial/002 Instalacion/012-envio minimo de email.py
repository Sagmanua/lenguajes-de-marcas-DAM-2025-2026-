import smtplib
from email.message import EmailMessage

# Configuración para Resend
SMTP_SERVER = "smtp.resend.com"
SMTP_PORT = 465  # Resend recomienda SSL en el puerto 465

# El usuario en Resend SIEMPRE es "resend"
SMTP_USER = "resend" 
# Tu API Key (ejemplo: re_123456789)
SMTP_PASS = "123" 

msg = EmailMessage()
msg["From"] = "onboarding@resend.dev" # O un dominio verificado en tu cuenta
msg["To"] = "sidorenko.bogdan.05@gmail.com"
msg["Subject"] = "Esto es un ejercicio de clase (vía Resend)"
msg.set_content("Hola, esto es una prueba desde Python usando Resend.\n")

# Usamos SMTP_SSL para el puerto 465
with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
    smtp.login(SMTP_USER, SMTP_PASS)
    smtp.send_message(msg)

print("Email sent via Resend")