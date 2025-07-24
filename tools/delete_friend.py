from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class DeleteFriendInput(BaseModel):
    friend_id: int = Field(..., description="The ID of the friend to delete.")

def delete_friend(friend_id: int):
    """Delete a friend from Splitwise by their ID."""
    api = SplitwiseAPI()
    return api.delete_friend(friend_id)
