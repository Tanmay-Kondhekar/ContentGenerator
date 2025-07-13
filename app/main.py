from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from app.helpers import models, database
import app.router as router

models.BASE.metadata.create_all(bind=database.engine)

app = FastAPI()
templates = Jinja2Templates(directory="app/templates")

app.include_router(router.router)