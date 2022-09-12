from abc import ABC
from datetime import datetime
from typing import Optional, List, Union

from pydantic import parse_obj_as

from .methods import GetBalance, GetProxyList, GetOrders, RenewProxy, OrderProxy, GetCountries, GetIPs, GetIPsCount, \
    GetOrderPrice
from ..core.abc import BaseAPIClient
from ..types import Balance, ProxyStatus, ProxyType, ProxyProtocol, Countries, ProxyFormat, IPs, IPsCount, OrderPrice, \
    ProxyList, ProxyInfo, Order


class ProxyLine(BaseAPIClient, ABC):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    async def get_balance(self) -> Balance:
        """
        Get balance
        :return: Account balance information
        :rtype: Balance
        """
        result = await self._send_request(GetBalance)
        return Balance(**result)

    async def get_proxy_list(self, status: Optional[ProxyStatus] = None, proxy_type: Optional[ProxyType] = None,
                             ip_version: Optional[ProxyProtocol] = None, country: Optional[str] = None,
                             date_end_after: Optional[datetime] = None, date_end_before: Optional[datetime] = None,
                             date_after: Optional[datetime] = None, date_before: Optional[datetime] = None,
                             orders: Optional[Union[List[int], int]] = None,
                             proxy_format: Optional[ProxyFormat] = None,
                             limit: Optional[int] = 200,
                             offset: Optional[int] = 0) -> ProxyList:
        """
        Get proxy list
        :param status: Status
        :param proxy_type: Type
        :param ip_version: IP version
        :param country: Country
        :param date_after: Date after
        :param date_before: Date before
        :param date_end_after: Date end after
        :param date_end_before: Date end before
        :param orders: Orders
        :param proxy_format: Format
        :param limit: Limit
        :param offset: Offset
        :return: List of proxies
        :rtype: ProxyList
        """
        data = {
            'status': status.value if status else None,
            'type': proxy_type.value if proxy_type else None,
            'ip_version': ip_version.value if ip_version else None,
            'country': country,
            'date_after': date_after,
            'date_before': date_before,
            'date_end_after': date_end_after,
            'date_end_before': date_end_before,
            'orders': orders,
            'format': proxy_format.value if proxy_format else None,
            'limit': limit,
            'offset': offset
        }
        result = await self._send_request(GetProxyList, data)
        modified_result = self._modify_proxy_list_json(result)
        return ProxyList(**modified_result)

    async def get_orders(self, date_after: Optional[datetime] = None,
                         date_before: Optional[datetime] = None) -> List[Order]:
        """
        Get Orders
        :param date_after: Date after
        :param date_before: Date before
        :return: List of orders
        :rtype: List[Order]
        """
        data = {
            'date_after': date_after,
            'date_before': date_before
        }
        result = await self._send_request(GetOrders, data)
        return parse_obj_as(List[Order], result)

    async def renew_proxy(self, proxy: Union[List[int], int], period: int,
                          coupon: Optional[str] = None) -> List[ProxyInfo]:
        """
        Renew proxy
        :param proxy: Proxy ID
        :param period: Renew period
        :param coupon: Coupon
        :return: Proxy Information
        :rtype: List[ProxyInfo]
        """
        data = {
            'proxies': proxy,
            'period': period,
            'coupon': coupon
        }
        result = await self._send_request(RenewProxy, data)
        modified_json = self._modify_renew_proxy_json(result)
        return parse_obj_as(List[ProxyInfo], modified_json)

    async def order_proxy(self, proxy_type: ProxyType, ip_version: ProxyProtocol, country: str,
                          period: int, quantity: int, coupon: Optional[str] = None,
                          ip_list: Optional[List[int]] = None) -> List[ProxyInfo]:
        """
        Order proxy
        :param quantity: Quantity
        :param ip_list: IP List received from ips method
        :param proxy_type: Proxy Type
        :param ip_version: IP version
        :param country: Country
        :param period: Period
        :param coupon: Coupon
        :return: Proxy Information
        :rtype: List[ProxyInfo]
        """
        data = {
            'type': proxy_type.value,
            'ip_version': ip_version.value,
            'country': country,
            'period': period,
            'ip_list': ip_list,
            'quantity': quantity,
            'coupon': coupon
        }
        result = await self._send_request(OrderProxy, data)
        modified_json = self._modify_renew_proxy_json(result)
        return parse_obj_as(List[ProxyInfo], modified_json)

    async def get_order_price(self, proxy_type: ProxyType, ip_version: ProxyProtocol, country: str,
                              period: int, quantity: int, coupon: Optional[str] = None,
                              ip_list: Optional[List[int]] = None) -> OrderPrice:
        """
        Get Proxy Order Price
        :param quantity: Quantity
        :param ip_list: IP List received from ips method
        :param proxy_type: Proxy Type
        :param ip_version: IP version
        :param country: Country
        :param period: Period
        :param coupon: Coupon
        :return: Order Price
        :rtype: OrderPrice
        """
        data = {
            'type': proxy_type.value,
            'ip_version': ip_version.value,
            'country': country,
            'period': period,
            'ip_list': ip_list,
            'quantity': quantity,
            'coupon': coupon
        }
        result = await self._send_request(GetOrderPrice, data)
        return OrderPrice(**result)

    async def get_countries(self) -> List[Countries]:
        """
        Get countries
        :return: Countries info
        :rtype: List[Countries]
        """
        result = await self._send_request(GetCountries)
        return parse_obj_as(List[Countries], result)

    async def get_ips(self, proxy_type: ProxyType, ip_version: ProxyProtocol, country: str,
                      city: Optional[str] = None) -> List[IPs]:
        """
        Get IPs
        :param city: City
        :param proxy_type: Proxy Type
        :param ip_version: IP version
        :param country: Country
        :return: List of IPs
        :rtype: List[IPs]
        """
        data = {
            'type': proxy_type.value,
            'ip_version': ip_version.value,
            'country': country,
            'city': city
        }
        result = await self._send_request(GetIPs, data)
        return parse_obj_as(List[IPs], result)

    async def get_ips_count(self, proxy_type: ProxyType, ip_version: ProxyProtocol, country: str,
                            city: Optional[str] = None) -> IPsCount:
        """
        Get IPs Count
        :param city: City
        :param proxy_type: Proxy Type
        :param ip_version: IP version
        :param country: Country name
        :return: IPs Count
        :rtype: IPsCount
        """
        data = {
            'type': proxy_type.value,
            'ip_version': ip_version.value,
            'country': country,
            'city': city
        }
        result = await self._send_request(GetIPsCount, data)
        return IPsCount(**result)

    @staticmethod
    def _modify_proxy_list_json(json: dict) -> dict:
        for result in json['results']:
            result['type'] = 'dedicated' if result['type'] == "1" else 'shared'
        return json

    @staticmethod
    def _modify_renew_proxy_json(json: dict) -> dict:
        for result in json:
            result['type'] = 'dedicated' if result['type'] == "1" else 'shared'
        return json
