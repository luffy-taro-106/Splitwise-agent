from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class GetGroupInput(BaseModel):
    group_id: int = Field(..., description="The ID of the group to retrieve.")

def get_group(group_id: int):
    """Get details for a specific group by its ID."""
    api = SplitwiseAPI()
    return api.get_group(group_id)
