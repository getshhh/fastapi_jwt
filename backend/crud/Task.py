from sqlalchemy.orm import Session
from models.Task import Task
from models.User import User
from fastapi import HTTPException, Depends
from crud.User import get_current_user

def create_task(db: Session, title: str, description: str,  current_user: User):
    task = Task(
        title=title,
        description=description,
        user_id=current_user.id  
    )
    db.add(task)
    db.commit()
    db.refresh(task)
    return {
        "Созданный заголовок": {title},
        "Созданный текст": {description}
    }

