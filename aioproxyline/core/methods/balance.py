from .base import APIMethod


class GetBalance(APIMethod):
    http_method = 'GET'
    path = '/balance/'
