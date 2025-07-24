from splitwise_api import SplitwiseAPI

def get_categories():
    """Get a list of all expense categories available in Splitwise."""
    api = SplitwiseAPI()
    return api.get_categories()
