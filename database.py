import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

if os.getenv("GITHUB_ACTIONS") is None:
    load_dotenv(".env.local")
    
# Ler variáveis de ambiente com fallback
user = "postgres"
password = "tiagoreis123"
database = "database_tigas"
host = "localhost"

# Debug: Verificar variáveis carregadas
print(f"DB_USER={user}")
print(f"DB_PASSWORD={'*' * len(password) if password else None}")
print(f"DB_NAME={database}")
print(f"DB_HOST={host}")

SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}/{database}"

# Log para verificar a URL de conexão
print(f"Database URL: {SQLALCHEMY_DATABASE_URL}")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
try:
    with engine.connect() as conn:
        print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")