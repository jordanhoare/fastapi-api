from fastapi import APIRouter, Depends
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from app.config import Settings, get_settings

router = APIRouter()

templates = Jinja2Templates(directory="templates")


@router.get("/home")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """
    Depends: depends on the result of get_settings
    settings: The value returned (Settings) is assigned for the return statements
    """
    return {
        "ping": "dong",
        "environment": settings.environment,
        "testing": settings.testing,
    }
