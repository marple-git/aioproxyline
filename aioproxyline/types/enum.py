from enum import Enum


class ProxyStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    DELETED = "deleted"


class ProxyType(str, Enum):
    DEDICATED = 'dedicated'
    SHARED = 'shared'


class ProxyProtocol(int, Enum):
    IP_V4 = 4
    IP_V6 = 6


class ProxyFormat(str, Enum):
    HTTP = 'txt-http'
    SOCKS5 = 'txt-socks5'
    CUSTOM_HTTP = 'custom-http'
    CUSTOM_SOCKS5 = 'custom-socks5'
