from typing import List

from pydantic import BaseModel


class SuggestSchema(BaseModel):
    content_id: str
    score: float


class UserSeenResponse(BaseModel):
    user_id: str
    event_type: str
    days: int
    seen: List[str]


class UserUnseenRequest(BaseModel):
    content_ids: List[str]


class UserUnseenResponse(BaseModel):
    unseen: List[str]


class UserSuggestResponse(BaseModel):
    suggested: List[SuggestSchema]
