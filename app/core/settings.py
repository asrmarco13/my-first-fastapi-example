from pydantic import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Example"
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 30
    SECRET_KEY: str = "83e241b98872a68640365c9d3f05da463f2ee38b7aea83ceb204fb628c70fd09"

    class Config:
        case_sensitive = True


settings = Settings()
