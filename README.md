# To-Do List com Django, PostgreSQL e React

Este projeto é uma aplicação **To-Do List** fullstack, desenvolvida para fins de estudo/avaliação. Ele utiliza:

* **Backend:** Django + Django REST Framework + PostgreSQL
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
DATABASE_URL=postgresql://appuser:apppass@127.0.0.1:5432/todolist
SECRET_KEY=django-insecure-change-me-in-production
DEBUG=True
```

### 5. Rodar migrações Django

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Criar superusuário (opcional)

```bash
python manage.py createsuperuser
```

### 7. Iniciar o servidor Django

```bash
python manage.py runserver
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

* [x] Backend com Django + PostgreSQL
* [x] ORM com Django ORM
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
4. Rode migrações Django e start backend
5. Rode frontend com `npm run dev`

## 🔧 Comandos Django Úteis

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Iniciar servidor de desenvolvimento
python manage.py runserver

# Acessar shell Django
python manage.py shell
```

---

## 📜 Licença

Uso acadêmico/educacional.
