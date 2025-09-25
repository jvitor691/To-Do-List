from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()


origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TaskIn(BaseModel):
    titulo: str
    descricao: str
    status: str = "pendente" 

class Task(TaskIn):
    id: int

DB: List[Task] = []
_next_id = 1

@app.get("/", tags=["health"])
def health():
    return {"mensagem": "Olá, FastAPI está rodando 🚀"}

@app.get("/tasks", response_model=List[Task], tags=["tasks"])
def list_tasks():
    return DB

@app.get("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: int):
    for t in DB:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task não encontrada")

@app.post("/tasks", response_model=Task, status_code=201, tags=["tasks"])
def create_task(data: TaskIn):
    global _next_id
    task = Task(id=_next_id, **data.model_dump())
    _next_id += 1
    DB.insert(0, task)
    return task

@app.put("/tasks/{task_id}", response_model=Task, tags=["tasks"])
def update_task(task_id: int, data: TaskIn):
    for i, t in enumerate(DB):
        if t.id == task_id:
            DB[i] = Task(id=task_id, **data.model_dump())
            return DB[i]
    raise HTTPException(status_code=404, detail="Task não encontrada")

@app.patch("/tasks/{task_id}/status", response_model=Task, tags=["tasks"])
def patch_status(task_id: int, status: str):
    if status not in ("pendente", "concluido"):
        raise HTTPException(status_code=400, detail="Status inválido")
    for i, t in enumerate(DB):
        if t.id == task_id:
            DB[i] = Task(id=task_id, titulo=t.titulo, descricao=t.descricao, status=status)
            return DB[i]
    raise HTTPException(status_code=404, detail="Task não encontrada")

@app.delete("/tasks/{task_id}", status_code=204, tags=["tasks"])
def delete_task(task_id: int):
    for i, t in enumerate(DB):
        if t.id == task_id:
            DB.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task não encontrada")
