from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, TIMESTAMP, ForeignKey, JSON, DATE, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Base
from app.users.profile.models import Role, Profile


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024),
        nullable=False
    )
    last_login: Mapped[datetime] = mapped_column(
        TIMESTAMP,
        default=datetime.utcnow
    )
    role_id: Mapped[int] = mapped_column(ForeignKey(Role.id))
    profile_id: Mapped[int] = mapped_column(ForeignKey(Profile.id))
    email: Mapped[str] = mapped_column(
        String(length=320),
        unique=True,
        index=True,
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(default=False, nullable=False)
