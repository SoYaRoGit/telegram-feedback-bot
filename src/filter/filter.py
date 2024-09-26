from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.methods import check_feedback


class IsFeedback(BaseFilter):
    """Фильтр проверки наличия отзыва"""

    async def __call__(self, message: Message):
        return await check_feedback(message.from_user.id)
