import abc


class APIMethod(abc.ABC):
    """
    Base API Method
    """
    http_method: str = "GET"
    path: str
