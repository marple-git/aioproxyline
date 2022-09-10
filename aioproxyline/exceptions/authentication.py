from .base import APIError


class WrongAPIKey(APIError):
    match = 'incorrect api key'
    text = 'Wrong API Key provided'
