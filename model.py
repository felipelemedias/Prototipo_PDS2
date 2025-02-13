from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, DateTime
from sqlalchemy.sql import text
from database import Base
from datetime import datetime

class Model_Mensagem(Base):
    __tablename__ = 'teste'

    id = Column(Integer, primary_key=True, nullable=False)
    titulo = Column(String, nullable=False)
    conteudo = Column(String, nullable=False)
    publicada = Column(Boolean, server_default='True', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)

class Model_MenuNav(Base):
    __tablename__ = 'menu_nav' 

    id = Column(Integer, primary_key=True, autoincrement=True)
    menuNav = Column(String, nullable=False)  
    link = Column(String, nullable=False) 
    created_at = Column(DateTime, default=datetime.utcnow) 
