# ✅ To-do API — FastAPI

API REST para gerenciamento de tarefas (To-do List), desenvolvida em Python utilizando FastAPI e SQLAlchemy.  
Este projeto faz parte do meu **portfólio de desenvolvimento backend**, com foco em boas práticas, organização de código e fundamentos de APIs REST.

---

## 🎯 Objetivo do projeto

O objetivo deste projeto é demonstrar:

- Criação de uma API REST do zero
- Organização profissional de um projeto backend
- Uso de FastAPI com SQLAlchemy
- Implementação de um CRUD completo
- Uso de validação de dados com Pydantic
- Escrita de testes automatizados básicos

---

## 🛠️ Tecnologias utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Pytest

---

## 📁 Estrutura do projeto

    └── todo-api/
        ├── app/
        │   ├── __init__.py  
        │   ├── main.py      # Rotas da API
        │   ├── database.py  # Conexão com o banco de dados
        │   ├── models.py    # Modelos do banco (SQLAlchemy)
        │   ├── schemas.py   # Validação de dados (Pydantic)
        │   └── crud.py      # Regras de negócio
        │
        ├── tests/
        │   └── test_tasks.py  # Testes automatizadas
        │
        ├── .venv/
        ├── requirements.txt
        └── README.md

---

## 🚀 Como executar o projeto

### Criar e ativar o ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Instalar as dependências

```bash
pip install -r requirements.txt
```

### Executar a API

```bash
uvicorn app.main:app --reload
```

## 📚 Documentação da API (Swagger)

Após iniciar o servidor, acesse no navegador: http://127.0.0.1:8000/docs

A documentação é gerada automaticamente pelo FastAPI.

---

## 🔌 Endpoints disponíveis

    Método | Rota        | Descrição
    GET	   | /tasks	     | Lista todas as tarefas
    POST   | /tasks	     | Cria uma nova tarefa
    GET    | /tasks/{id} | Busca uma tarefa por ID
    PUT    | /tasks/{id} | Atualiza uma tarefa
    DELETE | /tasks/{id} | Remove uma tarefa

---

## 🧪 Testes automatizados

Para rodar os testes:

```bash
pytest -v
```

## 📌 Próximos passos

- Adicionar autenticação (JWT)
- Criar paginação na listagem de tarefas
- Substituir SQLite por PostgreSQL
- Criar deploy em ambiente de produção