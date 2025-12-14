# ✅ To-do API — FastAPI & PostgreSQL

API REST para gerenciamento de tarefas (To-do List), desenvolvida em **Python** com **FastAPI**, **PostgreSQL**, **SQLAlchemy** e **JWT Authentication**.

Este projeto faz parte do meu **portfólio de desenvolvimento backend** e demonstra a construção de uma API completa, desde a arquitetura até o deploy em produção.

---

## 🌍 API em Produção

- **Base URL:** https://SEU-SERVICO.onrender.com  
- **Documentação (Swagger):** https://SEU-SERVICO.onrender.com/docs

> A API está hospedada no **Render**, utilizando PostgreSQL e variáveis de ambiente.

---

## 🎯 Objetivo do Projeto

Demonstrar, de forma prática, os principais fundamentos do desenvolvimento backend:

- Arquitetura em camadas (routers, services, repositories)
- CRUD completo com banco relacional
- Autenticação e autorização com JWT
- Boas práticas de organização de código
- Uso de migrações com Alembic
- Testes automatizados
- Deploy em ambiente de produção

---

## 🧠 Funcionalidades

### 🔐 Autenticação

- Cadastro de usuário
- Login com geração de token JWT
- Proteção de rotas autenticadas

### ✅ Tarefas (Tasks)

- Criar tarefa
- Listar tarefas do usuário autenticado
- Buscar tarefa por ID
- Atualizar tarefa
- Remover tarefa

> Cada usuário tem acesso **somente às suas próprias tarefas**.

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **PostgreSQL**
- **Alembic**
- **JWT (python-jose)**
- **Passlib (bcrypt)**
- **Pytest**
- **Docker (PostgreSQL local)**
- **Render (Deploy)**
- Python 3.10+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic
- Pytest

---

## 📁 Estrutura do Projeto



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

    todo-api/
    ├─ app/
    │  ├─ main.py
    │  ├─ database.py
    │  ├─ models.py
    │  ├─ schemas.py
    │  ├─ auth.py
    │  └─ deps.py
    │
    ├─ frontend/
    │  ├─ index.html      # login / cadastro
    │  ├─ tasks.html      # tela principal
    │  ├─ style.css
    │  └─ app.js
    │
    ├─ tests/
    │  └─ test_api.py
    │
    ├─ requirements.txt
    ├─ Dockerfile
    └─ README.md

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

## Dockerfile

```bash
docker build -t todo-api .  # Dar build na imagem
docker run -d --name todo-api-container -p 8000:8000 todo-api  # Rodar o container
```

## 📌 Próximos passos

- Adicionar autenticação (JWT)
- Criar paginação na listagem de tarefas
- Substituir SQLite por PostgreSQL
- Criar deploy em ambiente de produção