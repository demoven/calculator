import pytest
from app import app

@pytest.fixture
def client():
    """Configuration du client de test Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_success(client):
    """Teste si l'addition de 10 et 5 renvoie bien 15"""
    response = client.get('/add?a=10&b=5')
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['result'] == 15
    assert data['operation'] == 'addition'

def test_div_success(client):
    """Teste si la division de 10 par 2 renvoie bien 5"""
    response = client.get('/div?a=10&b=2')
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['result'] == 5

def test_div_by_zero(client):
    """Teste la sécurité : la division par zéro doit être bloquée"""
    response = client.get('/div?a=10&b=0')
    data = response.get_json()
    
    # On vérifie que l'API renvoie une erreur 400 (Bad Request)
    assert response.status_code == 400
    assert "error" in data
    assert data['error'] == "Division par zéro impossible"

def test_sub_success(client):
    """Teste si la soustraction de 10 et 5 renvoie bien 5"""
    response = client.get('/sub?a=10&b=5')
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['result'] == 5
    assert data['operation'] == 'soustraction'

def test_mul_success(client):
    """Teste si la multiplication de 10 et 5 renvoie bien 50"""
    response = client.get('/mul?a=10&b=5')
    data = response.get_json()
    
    assert response.status_code == 200
    assert data['result'] == 50
    assert data['operation'] == 'multiplication'

def test_invalid_params(client):
    """Teste si l'API gère les entrées qui ne sont pas des nombres"""
    response = client.get('/add?a=abc&b=5')
    assert response.status_code == 400