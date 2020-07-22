from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Example"
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 30
    SECRET_KEY: str = ""

    class Config:
        case_sensitive = True


settings = Settings()
