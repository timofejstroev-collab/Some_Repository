from fastapi import FastAPI
from src.transports.http_fastapi.routers import health_router
from src.utils.app_settings import get_app_settings


def create_fastapi_app() -> FastAPI:
    app = FastAPI(title=get_app_settings().app_title, debug=get_app_settings().app_debug)
    app.include_router(health_router)
    return app