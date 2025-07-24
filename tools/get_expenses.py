from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import Optional

class GetExpensesInput(BaseModel):
    group_id: Optional[int] = Field(None, description="The ID of a group to filter expenses by.")
    friend_id: Optional[int] = Field(None, description="The ID of a friend to filter expenses by.")
    dated_after: Optional[str] = Field(None, description="ISO 8601 timestamp to filter expenses after this date (e.g., '2024-01-01T00:00:00Z').")
    dated_before: Optional[str] = Field(None, description="ISO 8601 timestamp to filter expenses before this date (e.g., '2024-12-31T23:59:59Z').")
    limit: Optional[int] = Field(20, description="The maximum number of expenses to return. Defaults to 20.")

def get_expenses(group_id: Optional[int] = None, friend_id: Optional[int] = None, dated_after: Optional[str] = None, dated_before: Optional[str] = None, limit: int = 20):
    """Get a list of the current user's expenses. Can be filtered by group, friend, or date."""
    api = SplitwiseAPI()
    return api.get_expenses(group_id, friend_id, dated_after, dated_before, limit)
