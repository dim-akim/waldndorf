from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi_users import FastAPIUsers

from app.users.auth.models import User
from app.users.auth.schemas import UserRead, UserCreate
from app.users.auth.manager import get_user_manager
from app.users.auth.base_config import auth_backend
from app.users.profile.router import router as profile_router
from app.front.router import router as front_router

app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'), name='static')

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(front_router)
app.include_router(profile_router)
