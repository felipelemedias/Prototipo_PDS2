import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

if os.getenv("GITHUB_ACTIONS") is None:
    load_dotenv(".env.local")

DATABASE_URL = os.getenv("DATABASE_URL")  # Carregar a URL do banco de dados

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()