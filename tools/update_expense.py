from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import Optional

class UpdateExpenseInput(BaseModel):
    expense_id: int = Field(..., description="The ID of the expense to update.")
    group_id: Optional[int] = Field(None, description="The new group ID for the expense.")
    description: Optional[str] = Field(None, description="The new description for the expense.")
    cost: Optional[str] = Field(None, description="The new total cost of the expense.")

def update_expense(expense_id: int, group_id: Optional[int] = None, description: Optional[str] = None, cost: Optional[str] = None):
    """Update an existing expense in Splitwise. You must provide the expense ID and at least one field to update."""
    api = SplitwiseAPI()
    return api.update_expense(expense_id, group_id, description, cost)
