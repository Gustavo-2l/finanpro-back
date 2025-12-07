from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from core.database import get_db
from models.conta import Conta
from models.transacao import Transacao
from auth import get_current_user

router = APIRouter(tags=["Contas"])  # sem prefixo

# --- SCHEMA PARA RECEBER JSON ---
class ValorSchema(BaseModel):
    valor: float

# --- SALDO ---
@router.get("/saldo")
def ver_saldo(usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    conta = db.query(Conta).filter(Conta.user_id == usuario.id).first()
    if not conta:
        raise HTTPException(404, "Conta não encontrada")
    return {"saldo": conta.saldo}

# --- DEPOSITAR ---
@router.post("/depositar")
def depositar(dados: ValorSchema, usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    valor = dados.valor
    if valor <= 0:
        raise HTTPException(400, "Valor inválido")

    conta = db.query(Conta).filter(Conta.user_id == usuario.id).first()
    if not conta:
        raise HTTPException(404, "Conta não encontrada")

    conta.saldo += valor

    trans = Transacao(user_id=usuario.id, tipo="deposito", valor=valor)
    db.add(trans)
    db.commit()

    return {"msg": "Depósito realizado", "saldo_atual": conta.saldo}

# --- SACAR ---
@router.post("/sacar")
def sacar(dados: ValorSchema, usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    valor = dados.valor

    conta = db.query(Conta).filter(Conta.user_id == usuario.id).first()
    if not conta:
        raise HTTPException(404, "Conta não encontrada")

    if valor <= 0:
        raise HTTPException(400, "Valor inválido")
    if conta.saldo < valor:
        raise HTTPException(400, "Saldo insuficiente")

    conta.saldo -= valor

    trans = Transacao(user_id=usuario.id, tipo="saque", valor=valor)
    db.add(trans)
    db.commit()

    return {"msg": "Saque realizado", "saldo_atual": conta.saldo}

# --- HISTÓRICO ---
@router.get("/transacoes")
def historico(usuario = Depends(get_current_user), db: Session = Depends(get_db)):
    trans = db.query(Transacao).filter(Transacao.user_id == usuario.id).all()
    return trans
