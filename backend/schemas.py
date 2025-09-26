from pydantic import BaseModel
from typing import Literal , Optional

class TaskIn(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    status: Literal["pendente", "concluida"] = "pendente"

class TaskOut(TaskIn):
    id: int
    class Config:
        from_attributes = True

class StatusPatch(BaseModel):
    status: Literal["pendente", "concluida"]
    class Config:
        schema_extra = {
            "example": {
                "status": "concluida"
            }
        }
        