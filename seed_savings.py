from core.database import SessionLocal
from models.saving import Saving

# Cria a sessão com o banco
db = SessionLocal()

# Adiciona alguns savings de teste
db.add(Saving(value=1000, month="Janeiro"))
db.add(Saving(value=1500, month="Fevereiro"))
db.add(Saving(value=2000, month="Março"))

# Salva no banco
db.commit()

# Fecha a sessão
db.close()

print("Savings de teste adicionados!")
