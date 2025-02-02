from datetime import datetime, date

from sqlmodel import SQLModel, Field, Relationship, String, Column, JSON
from sqlalchemy.dialects import postgresql

from app.db import Base


class ParentsChildrenLink(SQLModel, table=True):
    __tablename__ = "parents_children_table"

    parent_id: int | None = Field(default=None, foreign_key="profiles.id", primary_key=True)
    child_id: int | None = Field(default=None, foreign_key="profiles.id", primary_key=True)


class Role(SQLModel, table=True):
    __tablename__ = "roles"

    id: int = Field(primary_key=True)
    name: str = Field(index=True)
    permissions: list[str] = Field(sa_column=Column(JSON))


# TODO сделать дополнительные таблицы для школьников и родителей
class Profile(Base, table=True):
    __tablename__ = "profiles"
    
    id: int | None = Field(default=None, primary_key=True)
    role_id: int = Field(default=None, foreign_key="roles.id")
    name: str
    family_name: str
    fathers_name: str
    birthday: date
    phone_number: str | None = Field(default=None, unique=True)
    tg_username: str | None = Field(default=None, unique=True)
    document_type: str | None
    document_number: str | None
    document_expiry: date | None
    children: list["Profile"] = Relationship(back_populates='parents', link_model=ParentsChildrenLink)
    parents: list["Profile"] = Relationship(back_populates='children', link_model=ParentsChildrenLink)


class ProfileIn(SQLModel):
    name: str
    phone: str
    kids: int


class ProfileOut(SQLModel):
    name: str
    phone: str
