# Backend/app/models/users.py
from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from datetime import datetime
from app.database import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)


class UserObject(BaseModel):
    id: int | None
    user_name: str | None
    email: str | None
    created_at: datetime | None
    updated_at: datetime | None
 
    class Config:
        from_attributes = True



class UserResponse(BaseModel):
    id: int | None
    user_name: str | None
    email: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        from_attributes = True


class UserCreate(BaseModel):
    user_name: str
    email: str


class UserUpdate(BaseModel):
    user_name: str = None
    email: str = None


class UserDelete(BaseModel):
    id: int | None
    email: str | None
