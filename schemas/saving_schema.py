from pydantic import BaseModel

class SavingBase(BaseModel):
    month: str
    value: int

class SavingResponse(SavingBase):
    id: int

    class Config:
        orm_mode = True
