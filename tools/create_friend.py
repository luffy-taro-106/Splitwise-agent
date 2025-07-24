from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import Optional

class CreateFriendInput(BaseModel):
    user_email: str = Field(..., description="Email address of the friend to add.")
    user_first_name: Optional[str] = Field(None, description="First name of the friend.")
    user_last_name: Optional[str] = Field(None, description="Last name of the friend.")

def create_friend(user_email: str, user_first_name: Optional[str] = None, user_last_name: Optional[str] = None):
    """Create a new friend in Splitwise. The email is required, first and last names are optional."""
    api = SplitwiseAPI()
    return api.create_friend(user_email, user_first_name, user_last_name)
