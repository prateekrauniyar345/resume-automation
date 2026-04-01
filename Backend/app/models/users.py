from sqlalchemy import Column, Integer, String, DateTime
from pydantic import BaseModel
from datetime import datetime
from app.database import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class UserObject(BaseModel):
    id: int | None
    username: str | None
    email: str | None
    created_at: datetime | None
    updated_at: datetime | None
 
    class Config:
        orm_mode = True



class UserResponse(BaseModel):
    id: int | None
    username: str | None
    email: str | None
    created_at: datetime | None
    updated_at: datetime | None

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: str


class UserUpdate(BaseModel):
    username: str = None
    email: str = None


class UserDelete(BaseModel):
    id: int | None
    email: str | None
