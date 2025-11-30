from fastapi import APIRouter

from ..schemas.users import (
    UserSeenResponse,
    UserUnseenRequest,
    UserUnseenResponse,
    UserSuggestResponse,
)


router = APIRouter(
    prefix="/users",
    tags=["👤 Users"],
)


@router.get(
    "/{id}/{event_type}/seen",
    summary="Возвращает все, что пользователь видел за указанное окно",
    response_model=UserSeenResponse,
)
async def user_seen(id: str, event_type: str, days: int): ...


@router.get(
    "/{id}/{event_type}/unseen",
    summary="Фильтрует список контента, возвращая только непросмотренное",
    response_model=UserUnseenResponse,
)
async def user_unseen(id: str, event_type: str, data: UserUnseenRequest): ...


@router.get(
    "/{id}/{event_type}/suggest",
    summary="Рекомендует \"непросмотренное + популярное сейчас\"",
    response_model=UserSuggestResponse,
)
async def user_suggest(id: str, event_type: str, limit: int): ...
