from fastapi import FastAPI, HTTPException, Depends
from db.db import Base, engine, get_session
from sqlalchemy.orm import Session
from jwt.JWT import OAuth2PasswordBearer, create_access_token

from crud.User import (
    register_user,
    login_user,
    info_me
)


app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.post("/register/")
def register(login: str, password: str, db: Session = Depends(get_session)):
    register_user(db, login, password)
    return f"Привет! {login}, регистрация прошла успешно"

@app.get("/login")
def login(login: str, password: str, db: Session = Depends(get_session)):
    user = login_user(db, login, password)
    access_token = create_access_token(
        data={"sub":user.login}
    )
    print(f"Токен для пользователя {user.login}: {access_token}")
    return {"message": f"С возвращением, {user.login}", "access_token": access_token}

@app.get("/me")
def me(id: int, db: Session = Depends(get_session)):
    return info_me(db, id)

