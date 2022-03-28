from app.config import Settings, get_settings
from fastapi import Depends, FastAPI

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    """
    Depends - depends on the result of get_settings
    settings: The value returned, Settings, is then assigned to the settings parameter
    """
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
