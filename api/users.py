from fastapi import Depends
from fastapi.routing import APIRouter
from typing import Annotated
from schemas.user import User
from controller.users import get_current_active_user

router = APIRouter()

@router.get("/me", response_model=User)
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):
    return current_user