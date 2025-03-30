from sqlalchemy import  DateTime, ForeignKey,Column, Integer, String, Boolean, Text, Enum, Index
from conexion import Base
from sqlalchemy.orm import relationship

import enum

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False) 
    correoElectronico = Column(String(100), nullable=False)
    contraseñaUsuario = Column(String(225), nullable=False)
    numeroCelular = Column(String(20))
    esAdmin = Column(Boolean, default=False)
    imagen = Column(String(225), nullable=True)

    # Relación con la tabla Reserva
    reservas = relationship("Reserva", back_populates="usuario", cascade="all, delete-orphan")
    # Relación con la tabla Pqr
    pqr_entries = relationship("Pqr", back_populates="usuario", cascade="all, delete-orphan")

class TipoPlan(enum.Enum):
    Recorrido = "Recorrido"
    Mesa = "Mesa"
    Camping = "Camping"
    Evento = "Evento"

class Reserva(Base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    plan_id = Column(Integer, ForeignKey("planes.id", ondelete="CASCADE"))
    fecha = Column(DateTime, nullable=False) 
    tipo_Reserva = Column(String(225), nullable=False) 
    tipo_Plan = Column(Enum(TipoPlan), nullable=False)
    Detalle = Column(String(225), nullable=False)
    pagada = Column(Boolean, default=False)

    usuario = relationship("Usuario", back_populates="reservas")
    
    plan = relationship("Plan", back_populates="reservas", lazy="joined")
    
    
class Pqr(Base):
    __tablename__ = "pqr"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    descripcion = Column(String(200), nullable=False)
    correo = Column(String(100), nullable=False) 
    respuesta = Column(String(255), nullable=True) 

    usuario = relationship("Usuario", back_populates="pqr_entries")



class Plan(Base):
    __tablename__ = 'planes'
    
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(50), nullable=False)
    descripcion = Column(Text)
    tipo = Column(Enum(TipoPlan), nullable=False) 
    cantidad_maxima = Column(Integer, nullable=False)
    cantidad_actual = Column(Integer, default=0)
    disponible = Column(Boolean, default=True)
    
    reservas = relationship("Reserva", back_populates="plan")