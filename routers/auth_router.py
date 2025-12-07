from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from schemas.login_schema import LoginSchema
from models.user import User
from models.conta import Conta
from schemas.user_schema import UserCreate
from core.database import get_db
from auth import gerar_hash_senha, verificar_senha, criar_token_acesso

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

router = APIRouter(tags=["Autenticação"])

@router.post("/register")
def registrar(user: UserCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(User).filter(User.email == user.email).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado.")

    senha_hash = gerar_hash_senha(user.senha)

    novo_usuario = User(
        nome=user.nome,
        email=user.email,
        senha=senha_hash
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    nova_conta = Conta(user_id=novo_usuario.id, saldo=0)
    db.add(nova_conta)
    db.commit()

    return {"msg": "Usuário registrado com sucesso!"}

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not verificar_senha(data.senha, user.senha):
        raise HTTPException(status_code=401, detail="Email ou senha incorretos")

    token = criar_token_acesso({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}
