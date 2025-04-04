import pytest
from app.api.app import *
from app.banco.scripts.db import *
@pytest.fixture
def client():
    """Configura o cliente de teste do Flask."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_listar_operadoras(client):
    """Testa a rota /operadoras."""
    response = client.get("/operadoras")
    assert response.status_code == 200
    assert isinstance(response.json, list)