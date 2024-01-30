from fastapi import FastAPI
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from settings import get_settings
from api.users import router as users_router
from api.token import router as token_router

settings    = get_settings()
app         = FastAPI()
# ! Enforce HTTPS connections
app.add_middleware(HTTPSRedirectMiddleware)
# ! Routes
app.include_router(users_router, prefix="/users")
app.include_router(token_router, prefix="/token")