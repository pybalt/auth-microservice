from . import settings

from datetime import timedelta
from fastapi.routing import APIRouter
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from schemas.token import Token
from controller.users import authenticate_user
from controller.token import create_access_token
from db.fake_db import fake_users_db
from utils.exceptions import InvalidCredentials

router = APIRouter()

ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

@router.post("/")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Token:
    """
    TODO: Protect this endpoint against brute force attacks
    
    https://fastapi.tiangolo.com/advanced/security/http-basic-auth/
    """
    
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user: 
        raise InvalidCredentials
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")