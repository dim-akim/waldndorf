from datetime import datetime

from sqlmodel import SQLModel, Field

from app.db import Base


class User(Base, table=True):
    __tablename__ = "users"

    id: int = Field(primary_key=True)
    username: str = Field(index=True)
    hashed_password: str
    last_login: datetime = Field(default=datetime.utcnow)
    role_id: int = Field(foreign_key='roles.id')
    profile_id: int = Field(foreign_key='profiles.id')
    email: str = Field(index=True)
    is_active: bool = Field(default=True)
    is_superuser: bool = Field(default=False)
    is_verified: bool = Field(default=False)
