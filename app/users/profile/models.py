from datetime import datetime
from typing import Optional

from sqlalchemy import String, TIMESTAMP, ForeignKey, JSON, DATE, Boolean, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base, EntityBase


association_table = Table(
    "association_table",
    Base.metadata,
    Column("parent_id", ForeignKey("profiles.id"), primary_key=True),
    Column("child_id", ForeignKey("profiles.id"), primary_key=True),
)


class Role(Base):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    permissions: Mapped[list[str]] = mapped_column(JSON, nullable=False)


# TODO сделать дополнительные таблицы для школьников и родителей
class Profile(EntityBase):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey(Role.id))
    name: Mapped[str]
    family_name: Mapped[str]
    fathers_name: Mapped[str]
    birthday: Mapped[datetime.date] = mapped_column(DATE)
    phone_number: Mapped[str] = mapped_column(unique=True)
    tg_username: Mapped[str] = mapped_column(unique=True)
    document_type: Mapped[Optional[str]]
    document_number: Mapped[Optional[str]]
    document_expiry: Mapped[Optional[datetime.date]] = mapped_column(DATE)
    children: Mapped[list["Profile"]] = relationship(secondary=association_table, back_populates='parents')
    parents: Mapped[list["Profile"]] = relationship(secondary=association_table, back_populates='children')
