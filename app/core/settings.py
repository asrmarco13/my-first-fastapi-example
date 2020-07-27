from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    App settings
    """

    PROJECT_NAME: str = "FastAPI Example"
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 30
    SECRET_KEY: str = "<run: openssl rand -hex 32>"

    class Config:
        """
        Provide configurations to Pydantic
        """

        case_sensitive = True


settings = Settings()
