from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class UserIdentifier(BaseModel):
    id: Optional[int] = Field(None, description="User ID of the member to add.")
    email: Optional[str] = Field(None, description="Email of the member to add.")
    first_name: Optional[str] = Field(None, description="First name of the member.")
    last_name: Optional[str] = Field(None, description="Last name of the member.")

class CreateGroupInput(BaseModel):
    name: str = Field(..., description="The name of the group to create.")
    users: List[UserIdentifier] = Field(..., description="A list of users to add to the group. Identify each user by ID or email.")
    group_type: Optional[str] = Field("other", description="The type of group (e.g., 'trip', 'home', 'other'). Defaults to 'other'.")
    simplify_by_default: Optional[bool] = Field(True, description="Whether to enable debt simplification for this group by default.")

def create_group(name: str, users: List[UserIdentifier], group_type: str = "other", simplify_by_default: bool = True):
    """Create a new group in Splitwise. You must provide a name and a list of users to add."""
    api = SplitwiseAPI()
    users_list = [user.dict(exclude_none=True) for user in users]
    return api.create_group(name, users_list, group_type, simplify_by_default)
