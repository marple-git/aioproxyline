from .base import APIMethod


class GetProxyList(APIMethod):
    http_method = 'GET'
    path = '/proxies/'


class RenewProxy(APIMethod):
    http_method = 'POST'
    path = '/renew/'
