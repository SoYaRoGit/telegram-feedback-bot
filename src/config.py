from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    TELEGRAM_TOKEN: str

    class Сonfig:
        env_file = ".env"


settings = Settings()
