from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class UndeleteExpenseInput(BaseModel):
    expense_id: int = Field(..., description="The ID of the expense to restore.")

def undelete_expense(expense_id: int):
    """Restore a previously deleted expense in Splitwise by its ID."""
    api = SplitwiseAPI()
    return api.undelete_expense(expense_id)
