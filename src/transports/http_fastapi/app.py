from src.transports.http_fastapi.depends.app_factory import create_fastapi_app

def main():
    app = create_fastapi_app()
    return app
