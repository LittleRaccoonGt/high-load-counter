from datetime import datetime

from pydantic import BaseModel


class EventSchema(BaseModel):
    event_type: str
    content_id: str
    user_id: str
    timestamp: datetime
