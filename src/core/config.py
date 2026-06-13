from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Online Cinema API"
    API_V1_STR: str = "/api/v1"

    ENVIRONMENT: str = "development"

    SECRET_KEY: str = "dev_secret_key"

    DATABASE_URL: str = (
        "postgresql+asyncpg://postgres:postgres@localhost:5432/online_cinema"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

settings = Settings()
