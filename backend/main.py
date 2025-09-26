from fastapi import FastAPI, Depends, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select, desc
from sqlalchemy.orm import Session
from typing import List
import os

from db import get_db
from models import Task
from schemas import TaskIn, TaskOut, StatusPatch

app = FastAPI()

# CORS
origins_env = os.getenv("CORS_ORIGINS", "")
origins = [o.strip() for o in origins_env.split(",") if o.strip()] or [
    "http://127.0.0.1:5173", "http://localhost:5173",
    "http://127.0.0.1:3000", "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)



@app.get("/tasks", response_model=List[TaskOut], tags=["tasks"])
def list_tasks(db: Session = Depends(get_db)):
    tasks = db.execute(select(Task).order_by(desc(Task.id))).scalars().all()
    return tasks

@app.get("/tasks/{task_id}", response_model=TaskOut, tags=["tasks"])
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    return task

@app.post("/tasks", response_model=TaskOut, status_code=201, tags=["tasks"])
def create_task(data: TaskIn, db: Session = Depends(get_db)):
    task = Task(titulo=data.titulo, descricao=data.descricao, status=data.status)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@app.put("/tasks/{task_id}", response_model=TaskOut, tags=["tasks"])
def update_task(task_id: int, data: TaskIn, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    task.titulo = data.titulo
    task.descricao = data.descricao
    task.status = data.status
    db.commit()
    db.refresh(task)
    return task

@app.patch("/tasks/{task_id}/status", response_model=TaskOut, tags=["tasks"])
def patch_status(task_id: int, body: StatusPatch, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    task.status = body.status
    db.commit()
    db.refresh(task)
    return task

@app.delete("/tasks/{task_id}", status_code=204, tags=["tasks"])
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.get(Task, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task não encontrada")
    db.delete(task)
    db.commit()
    return Response(status_code=204)