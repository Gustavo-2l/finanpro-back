from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from auth import get_current_user
from models.user import User

router = APIRouter()

# Retorna dados fictícios de economia por mês
@router.get("/")
def get_savings(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    # Dados de exemplo (substitua depois pelo seu modelo de economia real)
    savings = [
        {"month": "JAN", "value": 500},
        {"month": "FEB", "value": 700},
        {"month": "MAR", "value": 300},
        {"month": "APR", "value": 1000},
    ]
    return savings
