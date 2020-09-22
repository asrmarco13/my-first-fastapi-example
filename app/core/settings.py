from typing import Optional, Any, Dict
from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    """
    App settings
    """

    PROJECT_NAME: str = "FastAPI Example"
    ACCESS_TOKEN_EXPIRES_MINUTES: int = 30
    SECRET_KEY: str = "<run: openssl rand -hex 32>"
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    POSTGRES_SERVER: str
    POSTGRES_PORT: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=values.get("DB_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            port=values.get("POSTGRES_PORT"),
            path=f"/{values.get('DB_NAME') or ''}",
        )

    class Config:
        """
        Provide configurations to Pydantic
        """

        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
