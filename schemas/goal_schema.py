from pydantic import BaseModel
from datetime import date


class GoalCreate(BaseModel):
    title: str
    description: str | None = None
    value: float
    deadline: date


class GoalResponse(BaseModel):
    id: int
    title: str
    description: str | None
    value: float
    deadline: date

    model_config = {
        "from_attributes": True
    }
