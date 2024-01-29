from dotenv import load_dotenv
from fastapi import FastAPI
from api.users import router as users_router
from api.token import router as token_router

load_dotenv()

app = FastAPI()
app.include_router(users_router, prefix="/users")
app.include_router(token_router, prefix="/token")