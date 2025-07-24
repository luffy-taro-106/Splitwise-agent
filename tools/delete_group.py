from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class DeleteGroupInput(BaseModel):
    group_id: int = Field(..., description="The ID of the group to delete.")

def delete_group(group_id: int):
    """Delete a group from Splitwise by its ID."""
    api = SplitwiseAPI()
    return api.delete_group(group_id)
