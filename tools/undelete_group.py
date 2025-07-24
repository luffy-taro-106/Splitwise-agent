from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field

class UndeleteGroupInput(BaseModel):
    group_id: int = Field(..., description="The ID of the group to restore.")

def undelete_group(group_id: int):
    """Restore a previously deleted group in Splitwise by its ID."""
    api = SplitwiseAPI()
    return api.undelete_group(group_id)
