from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

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
    plan_id:int
    fecha: datetime
    tipo_Reserva: str
    tipo_Plan: str
    Detalle: str
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
    
class TipoPlan(str, Enum):
    Recorrido = "Recorrido"
    Mesa = "Mesa"
    Camping = "Camping"
    Evento = "Evento"

class PlanBase(BaseModel):
    nombre: str
    descripcion: str
    tipo: TipoPlan
    cantidad_maxima: int

class PlanCreate(PlanBase):
    pass

class PlanResponse(PlanBase):
    id: int
    cantidad_actual: int
    disponible: bool

    class Config:
        orm_mode = True