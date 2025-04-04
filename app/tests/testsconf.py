import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from banco.scripts.models import Base
from banco.scripts.db import Session

TEST_DATABASE_URL = "postgresql+psycopg2://postgres:root@localhost:5432/intuitivecare_test"

@pytest.fixture(scope="module")
def test_engine():
    """Cria um engine para o banco de dados de teste."""
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(engine)
    yield engine
    Base.metadata.drop_all(engine)

@pytest.fixture(scope="function")
def test_session(test_engine):
    """Cria uma sessão para os testes."""
    Session = sessionmaker(bind=test_engine)
    session = Session()
    yield session
    session.close()