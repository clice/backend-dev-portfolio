"""
Testes da API de tarefas (To-do API).

Aqui testamos o comportamento da API como um cliente real,
fazendo requisições HTTP e analisando as respostas.
"""

from fastapi.testclient import TestClient
from app.main import app

# Cria um cliente de testes baseado na aplicação FastAPI
client = TestClient(app)


def test_list_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_task():
    response = client.post(
        "/tasks",
        json={"title": "Estudar FastAPI"}
    )
    assert response.status_code == 201
    assert response.json()["title"] == "Estudar FastAPI"
    
    
def test_get_task_not_found():
    response = client.get("/tasks/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"
    
    
def test_update_task():
    # Primeiro, cria uma tarefa
    create_response = client.post(
        "/tasks",
        json={"title": "Tarefa para atualizar"}
    )
    task_id = create_response.json()["id"]
    
    # Agora, atualiza a tarefa criada
    update_response = client.put(
        f"/tasks/{task_id}",
        json={
            "title": "Tarefa atualizada",
            "completed": True
        }
    )
    updated_task = update_response.json()
    assert updated_task["title"] == "Tarefa atualizada"
    assert updated_task["completed"] is True

    
def test_delete_task():
    # Primeiro, cria uma tarefa
    create_response = client.post(
        "/tasks",
        json={"title": "Tarefa para deletar"}
    )
    task_id = create_response.json()["id"]
    
    # Agora, deleta a tarefa criada
    delete_response = client.delete(f"/tasks/{task_id}")
    assert delete_response.status_code == 204
    
    # Verifica se a tarefa foi realmente deletada
    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 404
