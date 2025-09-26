# To-Do List com FastAPI, PostgreSQL e React

Este projeto é uma aplicação **To-Do List** fullstack, desenvolvida para fins de estudo/avaliação. Ele utiliza:

* **Backend:** FastAPI + SQLAlchemy + Alembic (migrações) + PostgreSQL
* **Frontend:** React (Vite) + Axios + Material UI Icons
* **Banco de Dados:** PostgreSQL

---

## 🚀 Funcionalidades

* Criar tarefas com título, descrição e status (pendente/concluído)
* Listar tarefas (ordenadas por ID desc)
* Editar tarefas existentes
* Alterar status via `PATCH`
* Excluir tarefas (com confirmação no frontend)
* Filtro de tarefas (todas/pendentes/concluídas)

---

## 📦 Pré-requisitos

* Python **3.11+**
* Node.js (versão LTS recomendada)
* PostgreSQL (rodando localmente)
* pgAdmin4 (opcional, para gerenciar o banco)

---

## ⚙️ Configuração do Backend

### 1. Crie o banco e usuário no PostgreSQL

```sql
CREATE ROLE appuser LOGIN PASSWORD 'apppass';
CREATE DATABASE todolist OWNER appuser;
GRANT ALL PRIVILEGES ON DATABASE todolist TO appuser;
```

### 2. Clone e entre no diretório

```bash
git clone https://github.com/jvitor691/To-Do-List.git
cd To-Do-List/backend
```

### 3. Crie o ambiente virtual e instale dependências

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1   # Windows
source .venv/bin/activate    # Linux/Mac
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure o arquivo `.env`

Crie `backend/.env`:

```
DATABASE_URL=postgresql+psycopg://appuser:apppass@127.0.0.1:5432/todolist
CORS_ORIGINS=http://127.0.0.1:5173,http://localhost:5173
SECRET_KEY=uma_chave_aleatoria
ALGORITHM=HS256
```

### 5. Rodar migrações Alembic

```bash
alembic upgrade head
```

### 6. Iniciar o servidor FastAPI

```bash
uvicorn main:app --reload
```

API disponível em `http://127.0.0.1:8000`.

---

## ⚛️ Configuração do Frontend

### 1. Instale dependências

```bash
cd ../frontend
npm install
```

### 2. Configure o arquivo `.env`

Crie `frontend/.env`:

```
VITE_API_URL=http://127.0.0.1:8000
```

### 3. Rode o frontend

```bash
npm run dev
```

Aplicação disponível em `http://127.0.0.1:5173`.

---

## 🔍 Rotas principais do Backend

* `GET /tasks` → lista todas as tarefas
* `POST /tasks` → cria uma nova tarefa
* `GET /tasks/{id}` → busca uma tarefa
* `PUT /tasks/{id}` → atualiza título/descrição/status
* `PATCH /tasks/{id}/status` → atualiza apenas o status
* `DELETE /tasks/{id}` → exclui tarefa

---

## ✅ Checklist de Requisitos Atendidos

* [x] Backend com FastAPI + PostgreSQL
* [x] ORM com SQLAlchemy + Alembic
* [x] CRUD completo
* [x] Frontend React consumindo a API
* [x] Axios configurado com baseURL dinâmica
* [x] Confirmação de exclusão no frontend
* [x] Filtro por status
* [x] Deploy local reprodutível

---

## 👩‍💻 Como contribuir/testar

1. Clone o repositório
2. Configure `.env` no backend e frontend
3. Crie o banco PostgreSQL
4. Rode migrações e start backend
5. Rode frontend com `npm run dev`

---

## 📜 Licença

Uso acadêmico/educacional.
