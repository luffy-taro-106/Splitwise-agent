from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class CreateCommentInput(BaseModel):
    expense_id: int = Field(..., description="The ID of the expense to add a comment to.")
    content: str = Field(..., description="The text content of the comment.")

def create_comment(expense_id: int, content: str):
    """Add a comment to a specific expense by its ID."""
    api = SplitwiseAPI()
    return api.create_comment(expense_id, content)
