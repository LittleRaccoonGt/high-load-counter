from fastapi import APIRouter

from ..schemas.content import ContentStatsResponse, ContentDetailsResponse, IsSeenResponse


router = APIRouter(
    prefix="/content",
    tags=["📰 Content"],
)


@router.get(
    "/{id}/stats",
    summary="Агрегированная статистика по контенту",
    response_model=ContentStatsResponse,
)
async def content_stats(id: str, event_type: str): ...


@router.get(
    "/{id}/details",
    summary="Sliding window контента",
    response_model=ContentDetailsResponse,
)
async def content_details(id: str, event_type: str, window: str):...


@router.get(
    "/{id}/is_seen",
    summary="Быстрая проверка \"видел ли юзер\"",
    response_model=IsSeenResponse,
)
async def is_seen(id: str, event_type: str, user_id: str): ...
