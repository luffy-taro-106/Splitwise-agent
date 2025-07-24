from splitwise_api import SplitwiseAPI

def get_members(group_id):
    """Get members of a specific group by ID"""
    api = SplitwiseAPI()
    return api.get_group_members(group_id)