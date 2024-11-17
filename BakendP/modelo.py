from sqlalchemy import String, Integer, Column, Date, Boolean, ForeignKey
from conexion import base
from sqlalchemy.orm import relationship

class Usuario(base):
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

class Reserva(base):
    __tablename__ = "reservas"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"))
    fecha = Column(Date, nullable=False)
    tipo_Reserva = Column(String(225), nullable=False)  
    pagada = Column(Boolean, default=False)

    usuario = relationship("Usuario", back_populates="reservas")

class Pqr(base):
    __tablename__ = "pqr"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False)
    descripcion = Column(String(200), nullable=False)
    correo = Column(String(100), nullable=False) 
    respuesta = Column(String(255), nullable=True) 

    usuario = relationship("Usuario", back_populates="pqr_entries")
