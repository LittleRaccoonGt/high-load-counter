from fastapi import APIRouter

from ..schemas.stats import StatsTrendingResponse, StatsTopResponse, StatsUniqueUsersResponse


router = APIRouter(
    prefix="/stats",
    tags=["📊 Statistics"],
)


@router.get(
    "/{event_type}/trending",
    summary="Самый популярный контент за указанное окно",
    response_model=StatsTrendingResponse,
)
async def stats_trending(event_type: str, window: str): ...


@router.get(
    "/{event_type}/top",
    summary="Топ контента за период",
    response_model=StatsTopResponse,
)
async def stats_top(event_type: str, limit: int, period: str): ...


@router.get(
    "/{event_type}/unique-users",
    summary="Сколько уникальных пользователей за указанный период совершили событие",
    response_model=StatsUniqueUsersResponse,
)
async def stats_unique_users(event_type: str, period: str): ...
