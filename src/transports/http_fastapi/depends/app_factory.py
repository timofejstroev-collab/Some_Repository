from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI(title="My API", debug=True)

    from src.transports.http_fastapi.routers import router

    app.include_router(router)

    return app