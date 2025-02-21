import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

database_user = os.getenv("DATABASE_USER")
database_name = os.getenv("DATABASE_NAME")
database_password = os.getenv("DATABASE_PASSWORD")
database_host = os.getenv("DATABASE_HOST")

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