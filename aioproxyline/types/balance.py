from pydantic import BaseModel


class Balance(BaseModel):
    """
    Balance Model
    """

    balance: float
    partner_balance: float
