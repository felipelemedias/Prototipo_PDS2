import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

if os.getenv("GITHUB_ACTIONS") is None:
    load_dotenv(".env.local")
    
# Ler variáveis de ambiente com fallback
POSTGRES_USER= 'postgres'
POSTGRES_PASSWORD='felipe'
POSTGRES_DB='pdsi2_database'
POSTGRES_HOST='postgres'

# Debug: Verificar variáveis carregadas
print(f"POSTGRES_USER={user}")
print(f"POSTGRES_PASSWORD={'*' * len(password) if password else None}")
print(f"POSTGRES_DB={database}")
print(f"POSTGRES_HOST={host}")

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