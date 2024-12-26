from .database import Base
from sqlalchemy import Integer, String, Boolean, text, ForeignKey
import datetime
from sqlalchemy.types import DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    published: Mapped[bool] = mapped_column(Boolean, server_default='TRUE', nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    owner_id : Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=False, server_default=func.now())
    phone_number: Mapped[str] = mapped_column(String, nullable=True)
    
class Vote(Base):
    __tablename__ = "votes"
    
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id', ondelete="CASCADE"), primary_key=True, nullable=False)
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey('posts.id', ondelete="CASCADE"), primary_key=True, nullable=False) 