from abc import ABC
from datetime import datetime
from typing import Optional, List, Union

from pydantic import parse_obj_as

from .methods import GetBalance, GetProxyList, GetOrders, RenewProxy, OrderProxy, GetCountries, GetIPs, GetIPsCount, \
    GetOrderPrice
from ..core.abc import BaseAPIClient
from ..types import Balance, ProxyStatus, ProxyType, ProxyProtocol, Countries, ProxyFormat, IPs, IPsCount, OrderPrice


class ProxyLine(BaseAPIClient, ABC):
    def __init__(self, api_key: str):
        super().__init__(api_key)

    async def get_balance(self) -> Balance:
        """
        Get balance
        :return: Balance
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
                             offset: Optional[int] = 0):
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
        # Todo: create pydantic basemodel for this method

    async def get_orders(self, date_after: Optional[datetime] = None,
                         date_before: Optional[datetime] = None):
        """
        Get Orders
        :param date_after: Date after
        :param date_before: Date before
        :return: List of orders
        """
        data = {
            'date_after': date_after,
            'date_before': date_before
        }
        result = await self._send_request(GetOrders, data)

    async def renew_proxy(self, proxy: Union[List[int], int], period: int,
                          coupon: Optional[str] = None):
        """
        Renew proxy
        :param proxy: Proxy ID
        :param period: Renew period
        :param coupon: Coupon
        :return: None
        """
        data = {
            'proxy': proxy,
            'period': period,
            'coupon': coupon
        }
        await self._send_request(RenewProxy, data)

    async def order_proxy(self, proxy_type: ProxyType, ip_version: ProxyProtocol, country: str,
                          period: int, coupon: Optional[str] = None,
                          ip_list: Optional[List[int]] = None):
        """
        Order proxy
        :param ip_list: IP List received from ips method
        :param proxy_type: Proxy Type
        :param ip_version: IP version
        :param country: Country
        :param period: Period
        :param coupon: Coupon
        :return: None
        """
        data = {
            'type': proxy_type.value,
            'ip_version': ip_version.value,
            'country': country,
            'period': period,
            'ip_list': ip_list,
            'coupon': coupon
        }
        result = await self._send_request(OrderProxy, data)

    async def get_order_price(self, proxy_type: ProxyType, ip_version: ProxyProtocol, country: str,
                              period: int, quantity: int, coupon: Optional[str] = None,
                              ip_list: Optional[List[int]] = None):
        """
        Get Proxy Order Price
        :param quantity: Quantity
        :param ip_list: IP List received from ips method
        :param proxy_type: Proxy Type
        :param ip_version: IP version
        :param country: Country
        :param period: Period
        :param coupon: Coupon
        :return: None
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
        :return: List of countries
        """
        result = await self._send_request(GetCountries)
        return parse_obj_as(List[Countries], result)

    async def get_ips(self, proxy_type: ProxyType, ip_version: ProxyProtocol, country: str,
                      city: Optional[str] = None):
        """
        Get IPs
        :param city: City
        :param proxy_type: Proxy Type
        :param ip_version: IP version
        :param country: Country
        :return: None
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
                            city: Optional[str] = None):
        """
        Get IPs Count
        :param city: City
        :param proxy_type: Proxy Type
        :param ip_version: IP version
        :param country: Country
        :return: None
        """
        data = {
            'type': proxy_type.value,
            'ip_version': ip_version.value,
            'country': country,
            'city': city
        }
        result = await self._send_request(GetIPsCount, data)
        return IPsCount(**result)
