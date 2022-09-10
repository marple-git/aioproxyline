from pydantic import BaseModel


class IPs(BaseModel):
    id: int
    ip: str


class IPsCount(BaseModel):
    count: int
