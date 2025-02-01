from datetime import date

from fastapi import APIRouter, Depends

from app.users.profile.dao import ProfileDAO


router = APIRouter(
    prefix="/profile",
    tags=["Профиль пользователя"]
)


@router.get('/{profile_id}')
async def get_profile(profile_id: int):
    result = await ProfileDAO.get_one_or_none(id=profile_id)
    return result


@router.put('/{profile_id}')
async def update_profile(profile_id: int):
    pass


@router.delete('/{profile_id}')
async def delete_profile(profile_id: int):
    pass
