from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class GetFriendInput(BaseModel):
    friend_id: int = Field(..., description="The ID of the friend to retrieve.")

def get_friend(friend_id: int):
    """Get details for a specific friend by their ID."""
    api = SplitwiseAPI()
    return api.get_friend(friend_id)
