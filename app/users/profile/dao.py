from datetime import date

from sqlalchemy import select, and_, func, or_, insert

from app.users.profile.models import Profile
from app.dao import BaseDAO
from app.db import async_session_maker, engine


class ProfileDAO(BaseDAO):
    model = Profile

    # @classmethod
    # async def get_all_with_images(cls,
    #                               user_id: int):
    #     query_get_bookings = (
    #         select(
    #             Booking.__table__.columns,
    #             Room.__table__.columns
    #         )
    #         .select_from(Booking)
    #         .outerjoin(Room, Booking.room_id == Room.id)
    #         .where(Booking.user_id == user_id)
    #     )
    #
    #     async with async_session_maker() as session:
    #         bookings = await session.execute(query_get_bookings)
    #         return bookings
