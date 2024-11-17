from typing import List
import bcrypt
from fastapi import FastAPI, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from conexion import crear, get_db
from modelo import base, Usuario, Reserva, Pqr
from schemas import RespuestaPQR, UsuarioBase as cli
from schemas import ReservaU as usu
from schemas import Login  # Asegúrate de tener este esquema definido
from schemas import PQRS
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
import os
from fastapi.staticfiles import StaticFiles
from schemas import ActualizarContraseña
from passlib.context import CryptContext


app = FastAPI()

#instalar pip install passlib
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app.mount("/imagenes", StaticFiles(directory="imagenes"), name="imagenes")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

base.metadata.create_all(bind=crear)

# CRUD de usuario 
@app.get("/usuarios/")
async def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

@app.post("/usuarios/", response_model=cli)
async def crear_usuario(usuario: cli, db: Session = Depends(get_db)):
    contraseña_encriptada = bcrypt.hashpw(usuario.contraseñaUsuario.encode('utf-8'), bcrypt.gensalt())
    
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        correoElectronico=usuario.correoElectronico,
        contraseñaUsuario=contraseña_encriptada.decode('utf-8'),
        numeroCelular=usuario.numeroCelular,
        esAdmin=usuario.esAdmin
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@app.put("/usuarios/{usuario_id}", response_model=cli)
async def actualizar_usuario(usuario_id: int, usuario_actualizado: cli, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    for key, value in usuario_actualizado.dict().items():
        setattr(usuario, key, value)

    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete("/usuarios/{usuario_id}", response_model=cli)
async def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    
    db.delete(usuario)
    db.commit()
    return usuario

# CRUD de reservas
@app.get("/reservas/")
async def obtener_reservas(db: Session = Depends(get_db)):
    reservas = db.query(Reserva).all()
    return reservas

@app.post("/reservas/", response_model=usu)
async def crear_reserva(reserva: usu, db: Session = Depends(get_db)):
    nueva_reserva = Reserva(**reserva.dict())
    db.add(nueva_reserva)
    db.commit()
    db.refresh(nueva_reserva)
    return nueva_reserva

@app.get("/reservas/{reserva_id}", response_model=usu)
async def obtener_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    return reserva

@app.put("/reservas/{reserva_id}", response_model=usu)
async def actualizar_reserva(reserva_id: int, reserva_actualizada: usu, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    for key, value in reserva_actualizada.dict().items():
        setattr(reserva, key, value)

    db.commit()
    db.refresh(reserva)
    return reserva

@app.delete("/reservas/{reserva_id}", response_model=usu)
async def eliminar_reserva(reserva_id: int, db: Session = Depends(get_db)):
    reserva = db.query(Reserva).filter(Reserva.id == reserva_id).first()
    if reserva is None:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")
    
    db.delete(reserva)
    db.commit()
    return reserva

# Método de login adaptado
@app.post("/login")
async def login(user: Login, db: Session = Depends(get_db)):
    db_user = db.query(Usuario).filter(Usuario.correoElectronico == user.nombre_usuario).first()
    
    if db_user is None:
        raise HTTPException(status_code=400, detail="Usuario no existe")

    if not bcrypt.checkpw(user.password.encode('utf-8'), db_user.contraseñaUsuario.encode('utf-8')):
        raise HTTPException(status_code=400, detail="Contraseña incorrecta")
    
    return {
        "mensaje": "Inicio de sesión Ok",
        "nombre": db_user.nombre,
        "correoElectronico": db_user.correoElectronico,
        "numeroCelular":db_user.numeroCelular,
        "esAdmin":db_user.esAdmin,
        "id":db_user.id,
        "imagen":db_user.imagen,
    }

@app.post("/pqr/", response_model=PQRS)
async def crear_pqr(pqr: PQRS, db: Session = Depends(get_db)):
    nuevo_pqr = Pqr(**pqr.dict())
    db.add(nuevo_pqr)
    db.commit()
    db.refresh(nuevo_pqr)
    return nuevo_pqr

@app.get("/pqrs/", response_model=List[PQRS])  # Devuelve una lista de PQRs
async def obtener_pqrs(db: Session = Depends(get_db)):
    pqrs = db.query(Pqr).all()  # Consulta el modelo Pqr
    return pqrs

@app.get("/pqrs/{pqr_id}", response_model=PQRS)
async def obtener_pqr(pqr_id: int, db: Session = Depends(get_db)):
    pqr = db.query(Pqr).filter(Pqr.id == pqr_id).first()  # Consulta el modelo Pqr
    if pqr is None:
        raise HTTPException(status_code=404, detail="PQR no encontrado")
    return pqr

@app.put("/pqrs/{pqr_id}", response_model=PQRS)
async def actualizar_pqr(pqr_id: int, pqr_actualizado: PQRS, db: Session = Depends(get_db)):
    pqr = db.query(Pqr).filter(Pqr.id == pqr_id).first()  # Consulta el modelo Pqr
    if pqr is None:
        raise HTTPException(status_code=404, detail="PQR no encontrado")
    
    for key, value in pqr_actualizado.dict().items():
        setattr(pqr, key, value)

    db.commit()
    db.refresh(pqr)
    return pqr

@app.delete("/pqrs/{pqr_id}", response_model=PQRS)
async def eliminar_pqr(pqr_id: int, db: Session = Depends(get_db)):
    pqr = db.query(Pqr).filter(Pqr.id == pqr_id).first()  # Consulta el modelo Pqr
    if pqr is None:
        raise HTTPException(status_code=404, detail="PQR no encontrado")
    
    db.delete(pqr)
    db.commit()
    return pqr

@app.post("/usuarios/{user_id}/imagen")
async def subir_imagen_usuario(
    user_id: int,
    imagen: UploadFile = File(...),  # La imagen es ahora obligatoria para este endpoint
    db: Session = Depends(get_db)
):
    # Verificar si el usuario existe
    usuario = db.query(Usuario).filter(Usuario.id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Guardar la imagen
    imagen_path = f"imagenes/{imagen.filename}"
    os.makedirs(os.path.dirname(imagen_path), exist_ok=True)
    with open(imagen_path, "wb") as f:
        f.write(await imagen.read())

    # Actualizar el usuario con la nueva ruta de imagen
    usuario.imagen = imagen_path
    db.commit()
    db.refresh(usuario)

    return {"message": "Imagen actualizada exitosamente", "imagen_path": imagen_path}

@app.put("/pqrs/{pqr_id}/respuesta", response_model=PQRS)
async def responder_pqr(pqr_id: int, respuesta_pqr: RespuestaPQR, db: Session = Depends(get_db)):
    pqr = db.query(Pqr).filter(Pqr.id == pqr_id).first()
    if not pqr:
        raise HTTPException(status_code=404, detail="PQR no encontrado")
    
    pqr.respuesta = respuesta_pqr.respuesta
    db.commit()
    db.refresh(pqr)
    return pqr


@app.get("/usuarios/{usuario_id}/pqrs/respondidos", response_model=List[PQRS])
async def obtener_pqrs_respondidos(usuario_id: int, db: Session = Depends(get_db)):
    pqrs_respondidos = db.query(Pqr).filter(Pqr.usuario_id == usuario_id, Pqr.respuesta != None).all()
    if not pqrs_respondidos:
        raise HTTPException(status_code=404, detail="No se encontraron PQRs respondidos para este usuario")
    return pqrs_respondidos
from fastapi import Body

@app.put("/usuarios/{usuario_id}/correo", response_model=cli)
async def actualizar_correo_usuario(
    usuario_id: int, 
    nuevo_correo: str = Body(..., embed=True), 
    db: Session = Depends(get_db)
):
    """
    Actualiza el correo electrónico de un usuario específico.
    """
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Actualizar solo el correo electrónico
    usuario.correoElectronico = nuevo_correo
    db.commit()
    db.refresh(usuario)
    return usuario
@app.post("/usuarios/{usuario_id}/actualizar_contraseña")
def actualizar_contraseña(usuario_id: int, datos: ActualizarContraseña, db: Session = Depends(get_db)):
    # Obtener el usuario por ID
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Verificar la contraseña actual
    if not pwd_context.verify(datos.contraseñaActual, usuario.contraseñaUsuario):
        raise HTTPException(status_code=400, detail="La contraseña actual es incorrecta")

    # Actualizar la contraseña
    usuario.contraseñaUsuario = pwd_context.hash(datos.nuevaContraseña)
    db.commit()


    return {"message": "Contraseña actualizada exitosamente"}

@app.post("/reservas/{id}/pagar")
async def pagar_reserva(id: int, db: Session = Depends(get_db)):
    # Buscar la reserva por ID en la base de datos
    reserva = db.query(Reserva).filter(Reserva.id == id).first()
    
    if not reserva:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    if reserva.pagada:
        raise HTTPException(status_code=400, detail="La reserva ya está pagada")
    
    # Marcar la reserva como pagada
    reserva.pagada = True
    db.commit()  # Guardar los cambios en la base de datos
    db.refresh(reserva)  # Actualizar el objeto con los nuevos valores de la base de datos
    
    return {"id": reserva.id, "usuario_id": reserva.usuario_id, "fecha": reserva.fecha, "pagada": reserva.pagada}

@app.get("/reservas/{usuario_id}/user")
async def obtener_reservas(usuario_id: int, db: Session = Depends(get_db)):
    reservas = db.query(Reserva).filter(Reserva.usuario_id == usuario_id).all()
    if not reservas:
        raise HTTPException(status_code=404, detail="No hay reservas para este usuario")
    return reservas


