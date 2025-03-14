from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

load_dotenv()

# Configuración del servidor de correo
conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),  # Tu correo de Gmail
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),  # Tu contraseña de aplicación
    MAIL_FROM=os.getenv("MAIL_FROM"),         # Tu correo de Gmail
    MAIL_PORT=int(os.getenv("MAIL_PORT")),     # 587 para TLS
    MAIL_SERVER=os.getenv("MAIL_SERVER"),     # smtp.gmail.com
    MAIL_STARTTLS=True,                       # Usar TLS
    MAIL_SSL_TLS=False,                       # No usar SSL
    USE_CREDENTIALS=True                      # Usar credenciales
)

# Configuración para la solicitud de recuperación de contraseña
class EmailSchema(BaseModel):
    email: EmailStr

# Función para enviar el correo con el enlace de recuperación
async def send_reset_email(email: str, token: str):
    logger.debug(f"Preparando para enviar correo a: {email}")
    reset_url = f"http://localhost:5173/ResetPassword?token={token}"
    logger.debug(f"URL de recuperación: {reset_url}")

    message = MessageSchema(
        subject="Recuperación de contraseña",
        recipients=[email],
        body=f"""
        <h2>Recuperación de contraseña</h2>
        <p>Hemos recibido una solicitud para restablecer tu contraseña.</p>
        <p>Haz clic en el siguiente enlace para restablecerla:</p>
        <a href="{reset_url}">Restablecer contraseña</a>
        <p>Si no solicitaste este cambio, ignora este mensaje.</p>
        """,
        subtype="html"
    )

    try:
        fm = FastMail(conf)
        await fm.send_message(message)
        logger.info(f"Correo enviado exitosamente a: {email}")
    except Exception as e:
        logger.error(f"Error al enviar el correo: {e}")
        raise