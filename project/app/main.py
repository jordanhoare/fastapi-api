import logging

from fastapi import FastAPI

from app.api import ping, summaries
from app.db import init_db

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    """
    Routes:
        summaries: define a handler that expects a payload (SummaryPayloadSchema), with a URL.
        ping -> pong(): returns environment (dev, stage, prod) & testing config (y/n) of active pydantic BaseSetting

    + Include tags for grouping operations (https://swagger.io/docs/specification/grouping-operations-with-tags/)
    """
    application = FastAPI()
    application.include_router(ping.router)
    application.include_router(
        summaries.router, prefix="/summaries", tags=["summaries"]
    )
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
