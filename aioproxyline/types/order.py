from typing import List

from pydantic import BaseModel, Field

from .enum import ProxyType, ProxyProtocol


class PriceData(BaseModel):
    ip_list: List[str]
    period: int
    country: str
    type: ProxyType
    ip_version: ProxyProtocol
    quantity: int


class OrderPrice(BaseModel):
    price: float = Field(..., alias='amount')
    data: PriceData

