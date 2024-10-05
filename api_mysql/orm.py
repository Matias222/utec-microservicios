from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, Session
from dotenv import load_dotenv

import os

load_dotenv()

HOST = os.getenv('MYSQL_DB_URL')
DATABASE = os.getenv('MYSQL_DATABASE')
USER = os.getenv('MYSQL_USER')
PASSWORD = os.getenv('MYSQL_PASSWORD')

DATABASE_URL = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Cliente(Base):
    __tablename__ = "clientes"
    
    id_cliente = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    correo = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)
    
    pedidos = relationship("Pedido", back_populates="cliente", cascade="all, delete")

class Pedido(Base):
    __tablename__ = "pedidos"
    
    id_pedido = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente', ondelete="CASCADE"), nullable=False)
    fecha = Column(Date, nullable=False)
    total = Column(DECIMAL(10, 2), nullable=False)
    
    cliente = relationship("Cliente", back_populates="pedidos")
    detalles = relationship("DetallePedido", back_populates="pedido", cascade="all, delete")

class DetallePedido(Base):
    __tablename__ = "detalle_pedidos"
    
    id_detalle = Column(Integer, primary_key=True, index=True)
    id_pedido = Column(Integer, ForeignKey('pedidos.id_pedido', ondelete="CASCADE"), nullable=False)
    id_libro = Column(Integer, nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(DECIMAL(10, 2), nullable=False)
    
    pedido = relationship("Pedido", back_populates="detalles")

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()