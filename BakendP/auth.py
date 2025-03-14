from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from conexion import get_db
from modelo import Usuario
from passlib.context import CryptContext

# 🔐 Configuración del JWT
SECRET_KEY = "cambia_esto_por_una_clave_segura"  # Usa una clave segura
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# 🔑 Configurar esquema de autenticación
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 🔑 Función para generar un token JWT con todos los datos del usuario
def crear_token_jwt(usuario: Usuario, expires_delta: Optional[timedelta] = None):
    to_encode = {
        "sub": str(usuario.id),  # ID del usuario como string
        "nombre": usuario.nombre,  # Nombre completo
        "correoElectronico": usuario.correoElectronico,  # Correo del usuario
        "numeroCelular": usuario.numeroCelular,  # Teléfono (puede ser None)
        "esAdmin": usuario.esAdmin,  # Si es admin o no
        "imagen": usuario.imagen,  # Imagen de perfil (opcional)
        "exp": datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    }
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# 🔍 Función para verificar el token y extraer datos
def verificar_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        usuario_id: str = payload.get("sub")
        if usuario_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return payload  # Devuelve todos los datos del usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

# 🔑 Obtener usuario actual desde el token con todos los datos
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verificar_token(token)  # Obtiene todos los datos del token
    usuario_id = payload.get("sub")  # ID del usuario
    
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    return {
        "id": usuario.id,
        "nombre": usuario.nombre,
        "correoElectronico": usuario.correoElectronico,
        "numeroCelular": usuario.numeroCelular,
        "esAdmin": usuario.esAdmin,
        "imagen": usuario.imagen
    }
# token de recuperacion 
def generar_token_reset(user_id: int, email: str):
    # Define los datos que quieres incluir en el token
    payload = {
        "sub": email,  # El correo electrónico como identificador principal
        "user_id": user_id,  # El ID del usuario
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)  # Expiración
    }
    # Genera el token
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token
