import abc


class APIMethod(abc.ABC):
    http_method: str = "GET"
    path: str
