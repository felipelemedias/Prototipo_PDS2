import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

# Carrega variáveis do .env (exceto no GitHub Actions)
if os.getenv("GITHUB_ACTIONS") is None:
    load_dotenv(".env.local")

# Definição correta das variáveis
user = os.getenv("POSTGRES_USER", 'postgres')
password = os.getenv("POSTGRES_PASSWORD", 'felipe')
database = os.getenv("POSTGRES_DB", 'pdsi2_database')
host = os.getenv("POSTGRES_HOST", 'postgres')
port = os.getenv("POSTGRES_PORT", '5432')  # Coloquei porta também com default

# Debug: Verificar variáveis carregadas
print(f"POSTGRES_USER={user}")
print(f"POSTGRES_PASSWORD={'*' * len(password) if password else None}")
print(f"POSTGRES_DB={database}")
print(f"POSTGRES_HOST={host}")

# URL correta incluindo porta
SQLALCHEMY_DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{database}"

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

# Testa conexão
try:
    with engine.connect() as conn:
        print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco: {e}")
