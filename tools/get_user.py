from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class GetUserInput(BaseModel):
    user_id: int = Field(..., description="The ID of the user to retrieve.")

def get_user(user_id: int):
    """Get details for a specific user by their ID."""
    api = SplitwiseAPI()
    return api.get_user(user_id)
