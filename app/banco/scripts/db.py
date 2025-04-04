from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from banco.scripts.models import Base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = (
    f"{os.getenv('DB_DRIVER')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def criar_tabelas():
    Base.metadata.create_all(engine)
    print("✔ Tabelas criadas com sucesso!")