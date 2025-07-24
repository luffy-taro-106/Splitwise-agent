from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class GetCommentsInput(BaseModel):
    expense_id: int = Field(..., description="The ID of the expense to get comments for.")

def get_comments(expense_id: int):
    """Get all comments for a specific expense by its ID."""
    api = SplitwiseAPI()
    return api.get_comments(expense_id)
