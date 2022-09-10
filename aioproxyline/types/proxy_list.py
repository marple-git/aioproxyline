from typing import List

from pydantic import BaseModel


class ProxyList(BaseModel):
    count: int
    next: str
    previous: str
    results: List
