from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import Optional

class AddExpenseInput(BaseModel):
    description: str = Field(..., description="What the expense is for")
    amount: float = Field(..., description="Total cost of the expense")
    group_id: Optional[int] = Field(None, description="Numeric ID of the group to add the expense to. Leave empty for personal expenses.")
    payer_id: int = Field(..., description="Numeric ID of the user who paid for the expense")
    participants: list[int] = Field(..., description="A list of numeric user IDs for who to split the expense with")
    currency: Optional[str] = Field('INR', description="The currency code for the expense (e.g., 'USD', 'INR'). Defaults to INR.")

def add_expense(description: str, amount: float, payer_id: int, participants: list[int], group_id: Optional[int] = None, currency: str = 'INR'):
    """Add a new expense to Splitwise.
    
    Args:
        description: What the expense is for
        amount: Total cost of the expense
        payer_id: Numeric ID of the user who paid for the expense
        participants: List of numeric user IDs for who to split the expense with
        group_id: Optional numeric ID of the group to add the expense to. None for personal expenses.
        currency: Currency code (defaults to 'INR')
    """
    api = SplitwiseAPI()
    return api.create_expense(description, amount, group_id, payer_id, participants, currency_code=currency)
