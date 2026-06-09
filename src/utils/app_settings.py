from anyio.functools import lru_cache
from pydantic.v1 import BaseModel


class AppSettings(BaseModel):
    app_title: str = "My API"
    app_debug: bool = True

@lru_cache
def get_app_settings() -> AppSettings:
    return AppSettings()