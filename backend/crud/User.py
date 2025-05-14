from sqlalchemy.orm import Session
from models.User import User
from fastapi import HTTPException
from jwt.JWT import OAuth2PasswordBearer




def register_user(db: Session, login, password) -> str:
    is_admin = login.lower() == 'admin'
    user = User(login=login, password=password, admins=is_admin)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def login_user(db: Session, login, password) -> str:
    user = db.query(User).filter(User.login == login, User.password == password).first()
    if not user:
        raise HTTPException(status_code=402, detail="Неверные данные")
    return user


def info_me(db: Session, id: int):
    user = db.query(User).get(id)
    return user
