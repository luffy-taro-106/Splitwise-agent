from splitwise_api import SplitwiseAPI
from typing import List, Dict
from pydantic import BaseModel

class FriendInfo(BaseModel):
    id: int
    name: str
    email: str
    balance: List[Dict[str, float]]

def get_friends() -> List[FriendInfo]:
    """Get all friends with their details and balances"""
    api = SplitwiseAPI()
    return api.get_friends()