from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from datetime import datetime
from sqlalchemy.orm import relationship
from db.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, unique = True)
    login = Column(String, index = True, unique = True )
    password = Column(String, unique = True)
    created_at = Column(DateTime, default=datetime.utcnow)
    admins = Column(Boolean, default=False)
    tasks = relationship("Task", back_populates="user")
