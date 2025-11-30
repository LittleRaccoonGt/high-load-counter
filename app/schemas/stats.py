from typing import List

from pydantic import BaseModel


class TrendingItemSchema(BaseModel):
    content_id: str
    score: float


class TopItemSchema(BaseModel):
    content_id: str
    total: int
    unique: int


class StatsTrendingResponse(BaseModel):
    event_type: str
    window: str
    items: List[TrendingItemSchema]


class StatsTopResponse(BaseModel):
    event_type: str
    period: str
    limit: int
    items: List[TopItemSchema]


class StatsUniqueUsersResponse(BaseModel):
    event_type: str
    unique_users: int
