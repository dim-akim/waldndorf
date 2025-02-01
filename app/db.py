from datetime import datetime
from typing import AsyncGenerator

from sqlalchemy import TIMESTAMP, func
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from app.config import settings


engine = create_async_engine(settings.db_url)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    # __abstract__ = True
    #
    # @property
    # def __tablename__(self) -> str:
    #     return f'{self.__class__.__name__.lower()}s'
    pass


class EntityBase(Base):
    """Base class with fields related to all entities"""
    __abstract__ = True

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True),
                                                 server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True),
                                                 server_default=func.now(),
                                                 onupdate=func.now())
    is_deleted: Mapped[bool] = mapped_column(default=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
