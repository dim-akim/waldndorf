from datetime import date, datetime, timedelta

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


router = APIRouter(
    tags=["Frontend"]
)

templates = Jinja2Templates(directory="app/templates")


# @router.get('/hotels', response_class=HTMLResponse)
# async def get_hotels_page(
#         request: Request,
# ):
#     date_from = datetime.today().date()
#     date_to = (datetime.today() + timedelta(days=14)).date()
#     return templates.TemplateResponse(
#         request, "hotels.html",
#         context={
#             'hotels': [],
#             'hotel_location': '',
#             'date_from': date_from,
#             'date_to': date_to,
#             'dates': get_month_days()
#         }
#     )
#
#
# @router.get('/hotels/{hotel_location}', response_class=HTMLResponse)
# async def get_hotels_by_location_page(
#         request: Request,
#         hotel_location: str,
#         date_from: date,
#         date_to: date,
#         hotels=Depends(get_all_by_location)
# ):
#     return templates.TemplateResponse(
#         request, "hotels.html",
#         context={
#             'hotels': hotels,
#             'hotel_location': hotel_location,
#             'date_from': date_from,
#             'date_to': date_to,
#             'dates': get_month_days()
#         }
#     )


@router.get('/base', response_class=HTMLResponse)
async def get_base_page(request: Request):
    return templates.TemplateResponse(
        request,
        "user/waldbase.html"
    )


@router.get('/login', response_class=HTMLResponse)
async def get_login_page(request: Request):
    return templates.TemplateResponse(
        request,
        "user/login.html"
    )


@router.get('/profile', response_class=HTMLResponse)
async def get_profile_page(request: Request):
    return templates.TemplateResponse(
        request,
        "user/profile.html"
    )


@router.get('/registration', response_class=HTMLResponse)
async def get_registration_page(request: Request):
    return templates.TemplateResponse(
        request,
        "user/registration.html"
    )
