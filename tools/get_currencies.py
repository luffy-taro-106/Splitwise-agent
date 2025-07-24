from splitwise_api import SplitwiseAPI

def get_currencies():
    """Get a list of all currencies supported by Splitwise."""
    api = SplitwiseAPI()
    return api.get_currencies()
