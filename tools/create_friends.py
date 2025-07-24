from splitwise_api import SplitwiseAPI
from pydantic import BaseModel, Field
from typing import List, Optional

class FriendData(BaseModel):
    email: str = Field(..., description="Email address of the friend to add.")
    first_name: Optional[str] = Field(None, description="First name of the friend.")
    last_name: Optional[str] = Field(None, description="Last name of the friend.")

class CreateFriendsInput(BaseModel):
    friends: List[FriendData] = Field(..., description="A list of friends to create.")

def create_friends(friends: List[FriendData]):
    """Create multiple new friends in Splitwise at once. The email is required for each friend."""
    api = SplitwiseAPI()
    friends_list = [friend.dict(exclude_none=True) for friend in friends]
    return api.create_friends(friends_list)
