import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener las credenciales desde el .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME",)

# Crear la URL de conexión sin exponer credenciales en el código
URL_DB = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Crear la conexión con un pool de conexiones para mejor rendimiento
crear = create_engine(
    URL_DB,
    pool_size=10,  # Número de conexiones activas en el pool
    max_overflow=20,  # Número máximo de conexiones adicionales
    echo=False  # Cambia a True si quieres ver las consultas en la consola
)

# Configurar la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=crear)

# Base de datos declarativa
Base = declarative_base()

# Dependencia para obtener la sesión en los endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()