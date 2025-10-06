#📝 To-Do List — React (Vite) + Django (DRF, ORM do Django):

Aplicação de lista de tarefas com frontend em React e backend em Django (DRF).
O backend usa o ORM nativo do Django com migrações (makemigrations / migrate) e expõe rotas sem barra final (/tasks em vez de /tasks/) para compatibilidade com o front.

#✨ Funcionalidades:

Criar, listar, editar e excluir tarefas

Atualizar status (pendente / concluida) via PATCH

(Opcional) filtrar tarefas por status via query string

#🧱 Stack:

Frontend: React 18+, Vite, Axios

Backend: Django 5, Django REST Framework, django-cors-headers

Banco de dados: PostgreSQL

#📁 Estrutura do projeto
To-Do-List/
├─ backend/
│  ├─ manage.py
│  ├─ requirements.txt
│  ├─ todo/            # settings / urls / asgi / wsgi
│  └─ tasks/           # models / serializers / views / urls / admin / migrations
└─ frontend/           # app React (Vite)

#🚀 Como rodar o projeto
1️⃣ Backend (Django)
cd backend
python -m venv .venv
# Windows:
.\.venv\Scripts\Activate.ps1
# Linux/Mac:
source .venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver  # http://127.0.0.1:8000

📄 Arquivo .env
# Django
SECRET_KEY=django-insecure-change-me-in-production
DEBUG=True

# Banco (Postgres)
DATABASE_URL=postgresql://appuser:apppass@127.0.0.1:5432/todolist

2️⃣ Frontend (React + Vite)
cd ../frontend
npm install

# Configure a URL da API do backend
echo VITE_API_URL=http://127.0.0.1:8000 > .env

npm run dev  # http://127.0.0.1:5173

🔌 Endpoints principais (sem /api e sem barra final)
Método	Rota	Descrição
GET	/tasks	Lista tarefas
POST	/tasks	Cria tarefa ({ title, description?, status? })
GET	/tasks/{id}	Detalha tarefa
PUT	/tasks/{id}	Atualiza tarefa inteira
PATCH	/tasks/{id}/status	Atualiza apenas o status (pending/done)
DELETE	/tasks/{id}	Remove tarefa
💻 Exemplos (cURL)
# Listar
curl http://127.0.0.1:8000/tasks

# Criar
curl -X POST http://127.0.0.1:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Estudar ORM Django","description":"To-Do","status":"pending"}'

# Alterar status
curl -X PATCH http://127.0.0.1:8000/tasks/1/status \
  -H "Content-Type: application/json" \
  -d '{"status":"done"}'

⚙️ Notas importantes

Migrações: sempre gerar e versionar backend/tasks/migrations/.

CORS: habilitado para http://localhost:5173 em todo/settings.py.

Trailing slash: rotas sem / final por padrão (APPEND_SLASH=False).

Caso prefira com /, basta ajustar no urls.py e no front.

🧪 Troubleshooting
Problema	Solução
500 em POST /tasks	Confirme que APPEND_SLASH=False no settings.
Erro de CORS	Verifique CORS_ALLOWED_ORIGINS no settings.
Banco quebrado	Exclua o banco e rode makemigrations + migrate novamente.

#📄 Licença

Uso acadêmico e educacional. Livre para estudos, testes e portfólio.