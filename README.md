# To-Do List — React (Vite) + Django (DRF, ORM do Django)

Aplicação de lista de tarefas com **frontend React** e **backend Django**.  
O backend usa **ORM do Django** com **migrações nativas** (`makemigrations`/`migrate`) e expõe rotas **sem barra final** para compatibilidade com o front.

---

## ✨ Funcionalidades
- Criar, listar, editar e excluir tarefas
- Status: `pending` | `done`
- Atualização de status por `PATCH`
- (Opcional) filtro por status via query string

---

## 🧱 Stack
- **Frontend:** React 18+, Vite, Axios
- **Backend:** Django 5, Django REST Framework, django-cors-headers
- **Banco:** Postgres

---

## 📁 Estrutura sugerida
.
├─ backend_django/
│ ├─ manage.py
│ ├─ requirements.txt
│ ├─ todo/ # settings/urls/asgi/wsgi
│ └─ tasks/ # models/serializers/views/urls/admin/migrations
└─ frontend/ # app React (Vite)

yaml
Copiar código

---

## 🚀 Como rodar

### 1) Backend (Django)
```bash
cd backend_django
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver   # http://127.0.0.1:8000
2) Frontend (React + Vite)
bash
Copiar código
cd ../frontend
npm install
# Configure a URL da API do backend:
echo VITE_API_URL=http://127.0.0.1:8000 > .env
npm run dev   # http://127.0.0.1:5173
🔌 Endpoints (sem /api e sem barra final)
Método	Rota	Descrição
GET	/tasks	Lista tarefas
POST	/tasks	Cria { title, description?, status? }
GET	/tasks/{id}	Detalha tarefa
PUT	/tasks/{id}	Atualiza tarefa inteira
PATCH	/tasks/{id}/status	Atualiza apenas o status (pending/done)
DELETE	/tasks/{id}	Remove tarefa

Exemplos (cURL)
bash
Copiar código
# listar
curl http://127.0.0.1:8000/tasks

# criar
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Estudar ORM Django","description":"To-Do","status":"pending"}'

# mudar status
curl -X PATCH http://127.0.0.1:8000/tasks/1/status \
  -H "Content-Type: application/json" \
  -d '{"status":"done"}'
⚙️ Notas importantes
Migrações: sempre gerar e commitar backend_django/tasks/migrations/.

CORS: habilitado para http://localhost:5173 no todo/settings.py.

Trailing slash: as rotas aceitam sem barra final para casar com o front.

Se preferir com /, ajuste urls/router e o front.

🧪 Troubleshooting
500 em POST /tasks: confirme que as rotas aceitam sem barra final ou use APPEND_SLASH=False.

CORS bloqueando: revise CORS_ALLOWED_ORIGINS no todo/settings.py.

Reset do banco: apague db.sqlite3 e rode as migrações novamente.


📄 Licença
Uso acadêmico/educacional.