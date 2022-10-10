from email.policy import default
from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    role = Column(String)
    hashed_password = Column(String)
    status = Column(Boolean, default=False, nullable=False)
    