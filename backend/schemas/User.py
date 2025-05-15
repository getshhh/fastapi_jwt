from pydantic import BaseModel


class UserCreate(BaseModel):
    login: str
    password: str

class TokenResponse(BaseModel):
    message: str
    access_token: str
