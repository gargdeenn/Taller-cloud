from app.routes.user import router as user_router
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()




@app.middleware("http")
async def custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Custom-Header"] = "Custom header value"
    return response

async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"  # Cambia a tu origen permitido
    response.headers["Access-Control-Allow-Headers"] = "Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, OPTIONS"  # Cambia a tus métodos permitidos
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes cambiar esto para permitir orígenes específicos
    allow_credentials=True,
    allow_methods=["*"],  # Aquí puedes definir los métodos permitidos
    allow_headers=["*"],  # Aquí puedes definir los encabezados permitidos
)


@app.get("/")
async def root():
    return {"message": "La aplicacion esta funcionando!"}


app.include_router(user_router, prefix="/users", tags=["users"])
