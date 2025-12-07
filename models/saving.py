from sqlalchemy import Column, Integer, String
from core.database import Base

class Saving(Base):
    __tablename__ = "savings"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(String, unique=True, index=True)
    value = Column(Integer)
