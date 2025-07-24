from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class RemoveUserFromGroupInput(BaseModel):
    group_id: int = Field(..., description="The ID of the group to remove the user from.")
    user_id: int = Field(..., description="The ID of the user to remove.")

def remove_user_from_group(group_id: int, user_id: int):
    """Remove a user from a group in Splitwise. You must provide both the group ID and the user ID."""
    api = SplitwiseAPI()
    return api.remove_user_from_group(group_id, user_id)
