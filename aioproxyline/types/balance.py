from pydantic import BaseModel


class Balance(BaseModel):
    balance: float
    partner_balance: float
