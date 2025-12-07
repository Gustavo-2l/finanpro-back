from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from datetime import datetime
from core.database import Base

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    tipo = Column(String)  # deposito, saque
    valor = Column(Float)
    data = Column(DateTime, default=datetime.utcnow)
