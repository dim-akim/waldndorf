import enum
from datetime import datetime, date

from sqlmodel import SQLModel, Field, Enum, Column

from app.db import Base


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


class Event(Base, table=True):

    id: int = Field(primary_key=True)
    name: str = Field(unique=True, index=True)
    description: str
    short_description: str
    start_date: date
    end_date: date
    image_id: int


# TODO сделать дополнительные таблицы для школьников и родителей
class Application(Base, table=True):

    id: int = Field(primary_key=True)
    profile_id: int = Field(foreign_key='profiles.id')
    event_id: int = Field(foreign_key='events.id')
    parent_id: int | None = Field(default=None, foreign_key='users.id')
    school: str
    school_class: str
    have_medicine_issues: bool
    have_dietary_restrictions: bool
    medicine_issues: str
    dietary_restrictions: str
    sent_at: datetime
    status: str = Field(default=ApplicationStatus.DRAFT, sa_column=Column(Enum(ApplicationStatus)))
    payment_status: str = Field(default=PaymentStatus.NOT_PAID, sa_column=Column(Enum(PaymentStatus)))
