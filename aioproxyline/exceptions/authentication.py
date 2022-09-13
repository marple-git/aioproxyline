from .base import APIError


class WrongAPIKey(APIError):
    """Wrong API Key Exception"""

    match = 'incorrect api key'
    text = 'Wrong API Key provided'
