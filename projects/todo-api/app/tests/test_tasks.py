"""
Isso já prova:
- FastAPI rodando
- Endpoint funcionando
- Validação básica
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"title": "Test"})
    assert response.status_code == 200
