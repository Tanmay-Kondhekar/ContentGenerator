from fastapi import APIRouter, Request
import app.generate, app.analyze
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

router.include_router(app.generate.router, prefix="/generate", tags=["generate"])
router.include_router(app.analyze.router, prefix="/analyze", tags=["analyze"])