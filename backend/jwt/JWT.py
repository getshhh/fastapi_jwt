from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os


load_dotenv()

secret_key = os.environ.get("SECRET_KEY")


ALG = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data:dict, expires_delta: timedelta | None=None ):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    print("Истекает {expire}")
    print("Данные {to_encode}")
    encoded_token = jwt.encode(to_encode, secret_key, algorithm=ALG)
    print(f"Сгенерированный токен: {encoded_token}")
    return encoded_token

def verify_token(token: dict) -> str:
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALG])
        return payload
    except JWTError:
        raise HTTPException (
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Неверный токен"
        )
    
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")