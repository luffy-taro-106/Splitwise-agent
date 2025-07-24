from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import Optional

class GetNotificationsInput(BaseModel):
    limit: Optional[int] = Field(10, description="The maximum number of notifications to return. Defaults to 10.")

def get_notifications(limit: int = 10):
    """Get recent notifications for the current user."""
    api = SplitwiseAPI()
    return api.get_notifications(limit)
