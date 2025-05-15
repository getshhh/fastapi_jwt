from sqlalchemy.orm import Session
from models.User import User
from fastapi import HTTPException, Depends
from jwt.JWT import OAuth2PasswordBearer, oauth2_scheme, verify_token
from schemas.User import UserCreate
from db.db import Base, engine, get_session



def register_user(db: Session, login, password) -> UserCreate:
    is_admin = login.lower() == 'admin'
    user = User(login=login, password=password, admins=is_admin)

    user_check = db.query(User).filter(User.login == login).first()

    if user_check is not None:
        raise HTTPException (
            status_code=402,
            detail="Такой пользователь есть"
        )
    else:

        db.add(user)
        db.commit()
        db.refresh(user)
    return user


def login_user(db: Session, login, password) -> UserCreate:
    user = db.query(User).filter(User.login == login, User.password == password).first()
    if not user:
        raise HTTPException(status_code=402, detail="Неверные данные")
    return user


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_session)
) -> User:
    payload = verify_token(token)
    username: str = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=401, detail="Token invalid")
    
    user = db.query(User).filter(User.login == username).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user




