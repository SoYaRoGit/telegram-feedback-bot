from sqlalchemy import select

from database.database import Base, async_engine, async_session_factory
from database.models import Feedback


async def connect_database() -> None:
    """Подключение к базе данных"""
    async with async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)


async def create_feedback(user_id: int, user_name: str, text: str):
    """
    Функция для сохранения отзыва в базе данных

    Args:
        user_id (int): Telegram ID пользователя
        user_name (str) USER_NAME_TELEGRAM пользователя
        text_feedback (str): Текст отзыва от пользователя
    """
    async with async_session_factory() as db:
        feedback = Feedback(
            user_telegram_id=user_id, user_name=user_name, text_feedback=text
        )

        db.add(feedback)
        await db.commit()


async def check_feedback(user_id: int) -> bool:
    """Функция запрос к базе данных для проверки наличия отзыва у пользователя

    Args:
        user_id (int): user_id -> telegram_id

    Returns:
        bool: True если есть отзыв
    """
    async with async_session_factory() as db:
        result = await db.execute(select(Feedback).filter_by(user_telegram_id=user_id))
        feedback = result.scalars().first()
        return feedback is not None
