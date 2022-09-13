from .base import APIMethod


class GetBalance(APIMethod):
    """
    GetBalance Method
    """
    http_method = 'GET'
    path = '/balance/'
