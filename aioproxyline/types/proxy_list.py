from datetime import datetime
from typing import List, Union, Optional

from pydantic import BaseModel, Field

from .enum import ProxyProtocol, ProxyType


class ProxyTags(BaseModel):
    id: int
    name: str


class ProxyAccessIPs(BaseModel):
    id: int
    ip: str = Field(..., alias='value')
    name: Optional[str]


class ProxyInfo(BaseModel):
    id: int
    ip: str
    internal_ip: Optional[str]
    http_port: int = Field(..., alias='port_http')
    socks5_port: int = Field(..., alias='port_socks5')
    user: str
    username: str
    password: str
    order_id: int
    type: ProxyType
    ip_version: ProxyProtocol
    country: str
    date: datetime
    date_end: datetime
    tags: Optional[List[ProxyTags]]
    access_ips: Optional[List[ProxyAccessIPs]]


class ProxyList(BaseModel):
    count: int
    next: Optional[str]
    previous: Optional[str]
    results: List[ProxyInfo]
