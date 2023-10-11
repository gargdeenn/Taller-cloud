from fastapi import FastAPI

app = FastAPI()

# Importar los modelos para que sean detectados por Alembic
from app.models import *