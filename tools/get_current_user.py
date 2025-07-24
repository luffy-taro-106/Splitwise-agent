from splitwise_api import SplitwiseAPI

def get_current_user():
    """Get the current authenticated user's details"""
    api = SplitwiseAPI()
    return api.get_current_user()
