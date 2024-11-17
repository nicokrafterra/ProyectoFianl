from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioBase(BaseModel):
    id: Optional[int] = None  
    nombre: str
    correoElectronico: str
    contraseñaUsuario: str
    numeroCelular: str
    esAdmin: bool = False
    imagen: Optional[str] = None

class ReservaU(BaseModel):
    id: Optional[int] = None
    usuario_id: int
    fecha: date
    tipo_Reserva: str
    pagada: bool 
    
class Login(BaseModel):
   nombre_usuario:str
   password:str  
   
class PQRS(BaseModel):
    id: Optional[int] = None 
    usuario_id: int
    correo: str
    descripcion: str
    respuesta: Optional[str] = None

    class Config:
        orm_mode = True
        
class RespuestaPQR(BaseModel):
    respuesta: str  
class ActualizarContraseña(BaseModel):
    contraseñaActual: str
    nuevaContraseña: str