from enum import Enum
from typing import Union


class ProxyStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    DELETED = "deleted"


class ProxyType(Enum):
    DEDICATED = 'dedicated'
    SHARED = 'shared'


class ProxyProtocol(int, Enum):
    IPv4 = 4
    IPv6 = 6


class ProxyFormat(str, Enum):
    HTTP = 'txt-http'
    SOCKS5 = 'txt-socks5'
    CUSTOM_HTTP = 'custom-http'
    CUSTOM_SOCKS5 = 'custom-socks5'
