from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from auth import get_current_user
from models.user import User
from models.conta import Conta
from models.goal_models import Goal

router = APIRouter()

@router.get("/")
def dashboard_data(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):
    # SALDO
    conta = db.query(Conta).filter(Conta.user_id == user.id).first()
    if not conta:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    saldo = conta.saldo

    # DESPESAS (como não tem Expense, colocar 0)
    total_expenses = 0

    # METAS
    goals = db.query(Goal).filter(Goal.user_id == user.id).count()

    return {
        "saldo": saldo,
        "despesas": total_expenses,
        "metas_ativas": goals
    }
