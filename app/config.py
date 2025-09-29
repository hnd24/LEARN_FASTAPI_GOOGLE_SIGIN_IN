from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    google_client_id: str
    google_client_secret: str
    secret_key: str
    jwt_secret_key: str
    redirect_url: str
    frontend_url: str

    model_config = SettingsConfigDict(
        env_file=".env",               # << chỉ cần vậy
        env_file_encoding="utf-8",
        extra="ignore",
    )

settings = Settings()