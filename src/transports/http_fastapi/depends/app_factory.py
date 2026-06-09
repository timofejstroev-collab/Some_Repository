from fastapi import FastAPI
from src.transports.http_fastapi.routers import health_router

APP_TITLE = "My API"
APP_DEBUG = True

def create_fastapi_app() -> FastAPI:
    app = FastAPI(title=APP_TITLE, debug=APP_DEBUG)
    app.include_router(health_router)
    return app