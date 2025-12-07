### FinanPro 

### Visão Geral

O FinanPro é uma API RESTful desenvolvida em FastAPI para gerenciar contas, transações e suporte financeiro. Permite integração com um frontend (como React/Vite) para fornecer funcionalidades como:

Controle de saldo e transações

Criação e gerenciamento de metas

Autenticação de usuários

Integração com chat de suporte ou assistente virtual

### Tecnologias Utilizadas

Python 3.x

FastAPI 0.121.1 – framework web

Uvicorn 0.38.0 – servidor ASGI

SQLAlchemy 2.0.44 – ORM para banco de dados

python-jose 3.5.0 – criação e validação de tokens JWT

passlib 1.7.4 & bcrypt 3.2.2 – hash de senhas

python-dotenv – gerenciamento de variáveis de ambiente

email-validator 2.3.0 – validação de emails

### Estrutura de Pastas
finanpro-back/
├── main.py                 
├── core/
│   └── database.py         
├── models/
│   ├── user.py             
│   └── conta.py
    └── goal_models.py
    └── transacao.py
    └── saving.py        
├── schemas/
│   ├── user_schema.py      
│   └── saving_schema.py 
│   └── goal_schema.py  
│   └── login_schema.py
├── routers/
│   ├── auth_router.py             
│   └── conta_router.py   
│   └── dashboard_router.py  
│   └── goal_router.py  
│   └── savings_router.py         
├── services/  
│   ├── goal_service.py 
├── venv/                  
└── auth.py   
└── main.py 
└── requirements.txt
└── seed_savings.py  
└── README.md                

### Instalação Local

 ### Clone o repositório:

git clone https://github.com/Gustavo-2l/finanpro-back.git
cd finanpro-back


 ### Crie um ambiente virtual:

python -m venv venv
source venv/bin/activate     # Linux/Mac
venv\Scripts\activate        # Windows


### Instale as dependências:

pip install -r requirements.txt


Rode a aplicação localmente:

uvicorn main:app --reload --host 0.0.0.0 --port 8000


### Rotas da API
 Autenticação (/auth)

POST /auth/register – Criar novo usuário

POST /auth/login – Fazer login e gerar token JWT



 Contas (/contas)

GET /contas/saldo – Ver saldo da conta

POST /contas/depositar – Adicionar valor à conta

POST /contas/sacar – Retirar valor da conta

GET /contas/transacoes – Histórico de transações

Dashboard

GET /dashboard/dashboard - Ver dados do Dashboard

GET /dashboard/savings/ - Ver dados de economia por mês

Metas 

GET /goals/ - Listar metas 

POST /goals/ - Criar Meta

## Segurança

Senhas criptografadas com bcrypt via passlib

Autenticação JWT usando python-jose

Validação de dados de entrada com Pydantic

## Testes

Teste os endpoints usando o Swagger UI:

http://localhost:8000/docs


Ou usando ferramentas como Postman ou Insomnia.

## Deploy

Para Render, crie um Web Service com:

Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Configure variáveis de ambiente no painel do Render.

O backend ficará disponível em https://finanpro.onrender.com.

Observações

Use HTTPS para proteger o tráfego da API.

Não versionar o arquivo .env com segredos.

Garanta que o frontend aponte para a URL do backend no Render.