from fastapi import FastAPI, HTTPException, Depends
from db.db import Base, engine, get_session
from sqlalchemy.orm import Session
from jwt.JWT import (OAuth2PasswordBearer, 
                    create_access_token, 
                    verify_token, 
                    OAuth2PasswordRequestForm)
from schemas.User import UserCreate, TokenResponse

from crud.User import (
    register_user,
    login_user,
    get_current_user,
    User
)

from crud.Task import (
    create_task
)


app = FastAPI()

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.post("/register/")
def register(login, password, db: Session = Depends(get_session)) -> UserCreate:
    register_user(db, login, password)
    return f"Привет! {login}, регистрация прошла успешно"

@app.get("/login", response_model=TokenResponse)
def login(login, password, db: Session = Depends(get_session)) -> UserCreate:
    user = login_user(db, login, password)
    access_token = create_access_token(
        data={"sub":user.login}
    )
    print(f"Токен для пользователя {user.login}: {access_token}")
    return {"message": f"С возвращением, {user.login}", "access_token": access_token}



@app.post("/token")
def login_access(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if username != "user" or "password" != "password":
        raise HTTPException ( 
            status_code=400,
            detail="Неправльные данные"
        )
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/add_task")
def add_task_user(title: str, 
                description: str, 
                db: Session = Depends(get_session), 
                current_user: User = Depends(get_current_user)
                ):
    add_task = create_task(db, title, description, current_user)
    return {
        "message": f"С возвращением, {current_user.login}",
        "user": {
            "id": current_user.id,
            "login": current_user.login,
            "is_admin": current_user.admins,
            "add_task": add_task
        }
    }

@app.get("/me")
def me (current_user: User = Depends(get_current_user)):
    return {
        "message": f"С возвращением, {current_user.login}",
        "user": {
            "id": current_user.id,
            "login": current_user.login,
            "is_admin": current_user.admins
        }
    }
