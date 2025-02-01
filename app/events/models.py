import enum
from datetime import datetime

from sqlalchemy import String, TIMESTAMP, ForeignKey, JSON, DATE, Boolean, Enum
from sqlalchemy.orm import Mapped, mapped_column

from app.db import EntityBase
from app.users.auth.models import User
from app.users.profile.models import Profile


class ApplicationStatus(enum.Enum):
    DRAFT = 'draft'
    SENT = 'sent'
    ACCEPTED = 'accepted'
    CANCELLED = 'cancelled'
    DECLINED = 'declined'


class PaymentStatus(enum.Enum):
    NOT_PAID = 'not_paid'
    PART_PAID = 'part_paid'
    PRE_PAID = 'pre_paid'
    FULL_PAID = 'full_paid'
    RETURN_NEEDED = 'return_needed'
    REFUNDED = 'refunded'


class Event(EntityBase):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True, index=True)
    description: Mapped[str] = mapped_column(nullable=False)
    short_description: Mapped[str] = mapped_column(nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(DATE)
    end_date: Mapped[datetime.date] = mapped_column(DATE)
    image_id: Mapped[int]


# TODO сделать дополнительные таблицы для школьников и родителей
class Application(EntityBase):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    profile_id: Mapped[int] = mapped_column(ForeignKey(Profile.id))
    event_id: Mapped[int] = mapped_column(ForeignKey(Event.id))
    parent_id: Mapped[int] = mapped_column(ForeignKey(User.id), nullable=True)
    school: Mapped[str]
    school_class: Mapped[str]
    have_medicine_issues: Mapped[bool]
    have_dietary_restrictions: Mapped[bool]
    medicine_issues: Mapped[str]
    dietary_restrictions: Mapped[str]
    sent_at: Mapped[datetime] = mapped_column(TIMESTAMP)
    status: Mapped[str] = mapped_column(Enum(ApplicationStatus), default=ApplicationStatus.DRAFT)
    payment_status: Mapped[str] = mapped_column(Enum(PaymentStatus), default=PaymentStatus.NOT_PAID)
