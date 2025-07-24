from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class DeleteExpenseInput(BaseModel):
    expense_id: int = Field(..., description="The ID of the expense to delete.")

def delete_expense(expense_id: int):
    """Delete an expense from Splitwise by its ID."""
    api = SplitwiseAPI()
    return api.delete_expense(expense_id)
