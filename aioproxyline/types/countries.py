from typing import List

from pydantic import BaseModel, validator


class Cities(BaseModel):
    id: int
    name: str


class Countries(BaseModel):
    code: str
    name: str
    cities: List[Cities]
