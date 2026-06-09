from fastapi import FastAPI
from src.transports.http_fastapi.routers import router

def create_fastapi_app() -> FastAPI:
    app = FastAPI(title="My API", debug=True)
    app.include_router(router)

    return app