from fastapi import APIRouter, Response, status

from ..schemas.events import EventSchema


router = APIRouter(
    prefix="/events",
    tags=["🔔 Events"],
)


@router.post(
    "",
    summary="Запись события",
    response_class=Response,
)
async def event(data: EventSchema): ...
