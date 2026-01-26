import smtplib
from email.message import EmailMessage
import os

SMTP_SERVER = "smtp.resend.com"
SMTP_PORT = 465  

SMTP_USER = "resend"
SMTP_PASS = os.environ.get("RESEND_API_KEY") 

msg = EmailMessage()

msg["From"] = "onboarding@resend.dev" 
msg["To"] = "sidorenko.bogdan.05@gmail.com"
msg["Subject"] = "Informe de notas"

msg.set_content(
    "Este correo contiene un informe de notas en formato HTML.\n"
    "Si no lo ves correctamente, por favor usa un cliente de correo compatible."
)

html_content = """<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      td, th { padding: 5px; }
    </style>
  </head>
  <body>
    <table border="0" style="font-family:sans-serif; width:100%;">
      <tr>
        <td style="width:10%"></td>
        <td style="width:80%">
          <h1 style="text-align:center;">Informe de notas</h1>
          <p>Este es un informe de notas generado mediante la API de Resend.</p>
          <table border="0" width="100%">
            <tr style="background:indigo;color:white;">
              <th>Módulo profesional</th>
              <th>ACT</th><th>CONTROL</th><th>EVAL</th><th>COMP</th><th>TOT</th>
            </tr>
            <tr><td>Programación</td><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td></tr>
            <tr><td>Lenguajes de marcas</td><td>8</td><td>8</td><td>8</td><td>8</td><td>8</td></tr>
          </table>
          <h3 style="text-align:center;">Revisión de notas</h3>
          <p style="text-align:center;">Mañana martes 27 de enero a las 11:15</p>
        </td>
        <td style="width:10%"></td>
      </tr>
    </table>
  </body>
</html>"""

msg.add_alternative(html_content, subtype="html")

# --- Envío de email usando SMTP_SSL (Puerto 465) ---
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
        smtp.login(SMTP_USER, SMTP_PASS)
        smtp.send_message(msg)
    print("Email sent successfully via Resend")
except Exception as e:
    print(f"Error al enviar el email: {e}")