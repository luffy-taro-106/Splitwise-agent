from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import Optional

class AddUserToGroupInput(BaseModel):
    group_id: int = Field(..., description="The ID of the group to add the user to.")
    user_id: Optional[int] = Field(None, description="The ID of the user to add. Required if email is not provided.")
    email: Optional[str] = Field(None, description="The email of the user to add. Required if user_id is not provided.")
    first_name: Optional[str] = Field(None, description="The first name of the new user (if not already a Splitwise user).")
    last_name: Optional[str] = Field(None, description="The last name of the new user (if not already a Splitwise user).")

def add_user_to_group(group_id: int, user_id: Optional[int] = None, email: Optional[str] = None, first_name: Optional[str] = None, last_name: Optional[str] = None):
    """Add a user to a group in Splitwise. You must provide the group ID and either a user ID or an email address."""
    api = SplitwiseAPI()
    return api.add_user_to_group(group_id, user_id, first_name, last_name, email)
