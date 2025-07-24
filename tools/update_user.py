from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import Optional

class UpdateUserInput(BaseModel):
    user_id: int = Field(..., description="The ID of the user to update.")
    first_name: Optional[str] = Field(None, description="The user's new first name.")
    last_name: Optional[str] = Field(None, description="The user's new last name.")
    email: Optional[str] = Field(None, description="The user's new email address.")
    password: Optional[str] = Field(None, description="The user's new password. Be careful with this.")
    locale: Optional[str] = Field(None, description="The user's new locale (e.g., 'en_US').")
    default_currency: Optional[str] = Field(None, description="The user's new default currency code (e.g., 'USD').")

def update_user(user_id: int, first_name: Optional[str] = None, last_name: Optional[str] = None, email: Optional[str] = None, password: Optional[str] = None, locale: Optional[str] = None, default_currency: Optional[str] = None):
    """Update details for a specific user by their ID. Only include the fields you want to change."""
    api = SplitwiseAPI()
    return api.update_user(user_id, first_name, last_name, email, password, locale, default_currency)
