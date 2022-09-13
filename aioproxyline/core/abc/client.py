import abc
from typing import Optional, Type

from aiohttp import ClientSession, ContentTypeError

from ..methods.base import APIMethod
from ...exceptions import APIError


class BaseAPIClient(abc.ABC):
    """
    Base API Client
    """
    BASE_URL = 'https://panel.proxyline.net/api'

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def _send_request(self, method: Type[APIMethod], params: Optional[dict] = None) -> dict:
        """
        Send request to the API
        :param method: API Method
        :param params: Parameters
        :return: JSON
        """
        async with ClientSession() as session:
            params = self._delete_none(params or {})
            request_url = self._get_request_url(method)
            if method.http_method == 'GET':
                response = await session.get(request_url, params=params)
            else:
                response = await session.post(request_url, data=params)
            try:
                json = await response.json()
            except ContentTypeError as exception:
                raise APIError('Blocked by website ddos guard.') from exception
            if response.status in [403, 400]:
                if json.get('detail'):
                    APIError.detect(json['detail'])
                else:
                    APIError.detect(str(json))
            return json

    def _get_request_url(self, method: Type[APIMethod]) -> str:
        """
        Get url to send a request
        :param method: Method
        :return: URL
        """
        return f'{self.BASE_URL}{method.path}?api_key={self.api_key}'

    def _delete_none(self, _dict: dict) -> dict:
        """Delete None values recursively from all of the dictionaries"""
        for key, value in list(_dict.items()):
            if isinstance(value, dict):
                self._delete_none(value)
            elif value is None:
                del _dict[key]
            elif isinstance(value, list):
                for v_i in value:
                    if isinstance(v_i, dict):
                        self._delete_none(v_i)

        return _dict

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        return None
