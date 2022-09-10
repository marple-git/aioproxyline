from aioproxyline.core.methods import APIMethod


class GetCountries(APIMethod):
    http_method = 'GET'
    path = '/countries/'


class GetIPs(APIMethod):
    http_method = 'GET'
    path = '/ips/'


class GetIPsCount(APIMethod):
    http_method = 'GET'
    path = '/ips-count/'
