from . import settings

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Annotated
from passlib.context import CryptContext

from db.fake_db import fake_users_db
from schemas.user import UserInDB
from schemas.user import User
from schemas.token import TokenData
from utils.exceptions import InvalidCredentials, InactiveUser

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(fake_db, username: str, password: str):
    user = get_user(fake_db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def get_user(db, username: str):
    
    if username in db:
        user_dict = db[username]
        return UserInDB(**user_dict)

async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise InvalidCredentials
        token_data = TokenData(username=username)
    except JWTError:
        raise InvalidCredentials
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise InvalidCredentials
    return user

async def get_current_active_user(
    current_user: Annotated[User, Depends(get_current_user)]
):
    if current_user.disabled:
        raise InactiveUser
    return current_user

