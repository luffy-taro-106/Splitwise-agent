from splitwise_api import SplitwiseAPI

def get_balances(*args, **kwargs):
    """Get friend balances"""
    api = SplitwiseAPI()
    return api.get_friends()