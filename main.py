from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from core.database import Base, engine

from routers.auth_router import router as auth_router
from routers.conta_router import router as conta_router
from routers.dashboard_router import router as dashboard_router
from routers.savings_router import router as savings_router
from routers.goal_router import router as goals_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finanpro - API de Finanças")

# CORS para localhost + domínio do Vercel
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "https://finanpro-front-main-atualizado-lpaa.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Autenticação"])
app.include_router(conta_router, prefix="/contas", tags=["Contas"])
app.include_router(dashboard_router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(savings_router, prefix="/dashboard/savings", tags=["Dashboard"])
app.include_router(goals_router, prefix="/goals", tags=["Metas"])

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=app.title,
        version="1.0.0",
        description="API de Finanças",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    for path_item in openapi_schema["paths"].values():
        for operation in path_item.values():
            operation.setdefault("security", [{"BearerAuth": []}])

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
