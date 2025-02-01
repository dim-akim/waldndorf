from datetime import date, datetime, timedelta

from fastapi import APIRouter, Depends, Query, status

from app.events.dao import EventDAO, ApplicationDAO


router = APIRouter(
    prefix="/events",
    tags=["Мероприятия"]
)


@router.get("")
async def get_events(date_from: date = Query(description=f"Например, {date.today()}"),
                     date_to: date = Query(description=f"Например, {(datetime.now() + timedelta(days=14)).date()}")):
    pass


@router.get('/{event_id}')
async def get_event(event_id: int):
    result = await EventDAO.get_one_or_none(id=event_id)
    return result


@router.post('/{event_id}', status_code=status.HTTP_201_CREATED)
async def add_event(profile_id: int):
    pass


@router.put('/{event_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_event(profile_id: int):
    pass


@router.delete('/{event_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_event(profile_id: int):
    pass


@router.get('/{event_id}/application')
async def get_application(event_id: int):
    pass


@router.post('/{event_id}/application', status_code=status.HTTP_201_CREATED)
async def add_application(event_id: int):
    pass


@router.put('/{event_id}/application/{application_id}', status_code=status.HTTP_204_NO_CONTENT)
async def update_application(event_id: int):
    pass


@router.delete('/{event_id}/application/{application_id}')
async def delete_application(event_id: int):
    pass
