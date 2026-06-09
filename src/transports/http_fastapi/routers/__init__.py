from fastapi import APIRouter

from src.transports.http_fastapi.models import HealthResponse

health_router = APIRouter()

@health_router.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse(status="ok")