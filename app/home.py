from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi import Request

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})