from splitwise_api import SplitwiseAPI

def get_groups() -> list:
    """Returns a list of all groups with their members"""
    api = SplitwiseAPI()
    return api.get_groups()