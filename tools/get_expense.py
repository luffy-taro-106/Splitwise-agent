from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class GetExpenseInput(BaseModel):
    expense_id: int = Field(..., description="The ID of the expense to retrieve.")

def get_expense(expense_id: int):
    """Get details for a single expense by its ID."""
    api = SplitwiseAPI()
    return api.get_expense(expense_id)
