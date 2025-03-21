import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

if os.getenv("GITHUB_ACTIONS") is None:
    load_dotenv(".env.local")

POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'felipe'
POSTGRES_DB = 'pdsi2_database'
POSTGRES_HOST = 'localhost'

database_user = os.getenv("POSTGRES_USER")
database_name = os.getenv("POSTGRES_DB")
database_password = os.getenv("POSTGRES_PASSWORD")
database_host = os.getenv("POSTGRES_HOST")


print(f"postgresql://{database_user}:{database_password}@{database_host}/{database_name}")

SQLALCHEMY_DATABASE_URL = f"postgresql://{database_user}:{database_password}@{database_host}/{database_name}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()