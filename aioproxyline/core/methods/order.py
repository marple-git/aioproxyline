from .base import APIMethod


class GetOrders(APIMethod):
    http_method = 'GET'
    path = '/orders/'


class OrderProxy(APIMethod):
    http_method = 'POST'
    path = '/new-order/'


class GetOrderPrice(APIMethod):
    http_method = 'POST'
    path = '/new-order-amount/'
