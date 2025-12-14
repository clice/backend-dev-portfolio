from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user_and_login():
    # cria usuário
    resp = client.post(
        "/users",
        json={"username": "testuser", "password": "1234"},
    )
    assert resp.status_code in (201, 400)  # pode já existir em execuções repetidas

    # login
    resp = client.post(
        "/login",
        json={"username": "testuser", "password": "1234"},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


def test_create_and_list_tasks():
    # login (assumindo usuário testuser já existe)
    resp = client.post(
        "/login",
        json={"username": "testuser", "password": "1234"},
    )
    assert resp.status_code == 200
    token = resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # cria task
    resp = client.post(
        "/tasks",
        json={"title": "Minha primeira task", "description": "Testando", "completed": False},
        headers=headers,
    )
    assert resp.status_code == 201
    task = resp.json()
    assert task["title"] == "Minha primeira task"

    # lista tasks
    resp = client.get("/tasks", headers=headers)
    assert resp.status_code == 200
    tasks = resp.json()
    assert isinstance(tasks, list)
    assert any(t["title"] == "Minha primeira task" for t in tasks)
