from pydantic import BaseModel
from typing import Literal

class TaskIn(BaseModel):
    titulo: str
    descricao: str
    status: Literal["pendente", "concluido"] = "pendente"

class TaskOut(TaskIn):
    id: int
    class Config:
        from_attributes = True

class StatusPatch(BaseModel):
    status: Literal["pendente", "concluido"]
    class Config:
        schema_extra = {
            "example": {
                "status": "concluido"
            }
        }
        