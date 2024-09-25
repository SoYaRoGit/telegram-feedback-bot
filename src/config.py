from typing import Any, Dict

from pydantic import field_validator
from pydantic_settings import BaseSettings
from requests import Response, get


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str
    PROTECT_CONTENT: bool
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@localhost:5432/{self.POSTGRES_DB}"

    @field_validator("TELEGRAM_TOKEN", mode="before")
    def validate_telegram_token(cls, token: str) -> str:
        """валидатор для проверки действительности Телеграм-токена

        Returns:
            str: Действительный Телеграм-токен
        """
        url: str = f"https://api.telegram.org/bot{token}/getMe"

        response: Response = get(url)
        if response.status_code != 200:
            raise ValueError("Неверный TELEGRAM_TOKEN или токен недействителен.")

        data: Dict[str, Any] = response.json()

        if not data.get("ok", False):
            raise ValueError("Telegram API вернул ошибку при проверке токена.")

        return token

    class Config:
        env_file = ".env"


settings = Settings()
