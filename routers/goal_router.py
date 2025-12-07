# routers/goal_router.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List
from fastapi.security import OAuth2PasswordBearer

# Router
router = APIRouter()

# Modelo para criar meta
class GoalCreate(BaseModel):
    title: str
    value: float

# Modelo para retorno de meta
class Goal(BaseModel):
    title: str
    value: float

# Simulando banco de dados em memória
goals_db: List[Goal] = []

# Dependência de autenticação (simples para testar)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# =============================
# Criar nova meta
# =============================
@router.post("/", response_model=Goal, status_code=201)
async def create_goal(goal: GoalCreate, token: str = Depends(oauth2_scheme)):
    new_goal = Goal(title=goal.title, value=goal.value)
    goals_db.append(new_goal)
    return new_goal

# =============================
# Listar todas as metas
# =============================
@router.get("/", response_model=List[Goal])
async def list_goals(token: str = Depends(oauth2_scheme)):
    return goals_db
