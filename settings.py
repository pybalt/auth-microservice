from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name                        : str   = "Auth microservice"
    secret_key                      : str
    algorithm                       : str   = "HS256"
    access_token_expire_minutes     : int   = 30
    mongo_url                       : str
    model_config                    = SettingsConfigDict(env_file='.env')


@lru_cache
def get_settings():
    return Settings()