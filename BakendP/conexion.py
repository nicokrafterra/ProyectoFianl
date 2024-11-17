from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DB = "mysql+mysqlconnector://root:Tenno2006@localhost:3306/rproyecto"
crear= create_engine(URL_DB)
SessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=crear)
base= declarative_base()

def get_db():
    cnn=SessionLocal()
    try:
        yield cnn
    finally:
        cnn.close()
        