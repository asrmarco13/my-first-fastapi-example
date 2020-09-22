from typing import Optional
from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    """
    Properties token
    """

    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Payload properties
    """

    email: Optional[EmailStr] = None
