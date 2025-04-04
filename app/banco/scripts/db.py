from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from banco.scripts.models import Base

DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost:5432/intuitivecare"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def criar_tabelas():
    Base.metadata.create_all(engine)
    print("✔ Tabelas criadas com sucesso!")
    
