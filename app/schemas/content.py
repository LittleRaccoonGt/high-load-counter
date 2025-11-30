from typing import List
from datetime import datetime

from pydantic import BaseModel


class UniqueStatsSchema(BaseModel):
    h24: int
    d7: int
    d90: int


class TotalStatsSchema(BaseModel):
    h24: int
    d7: int
    all_time: int


class PointSchema(BaseModel):
    timestamp: datetime
    count: int


class ContentStatsResponse(BaseModel):
    content_id: str
    event_type: str
    unique: UniqueStatsSchema
    total: TotalStatsSchema
    trending_score: float


class ContentDetailsResponse(BaseModel):
    content_id: str
    event_type: str
    points: List[PointSchema]


class IsSeenResponse(BaseModel):
    seen: bool
