from fastapi import FastAPI

from src.transports.http_fastapi.depends.app_factory import create_fastapi_app


def main() -> FastAPI:
    return create_fastapi_app()
