from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from handler import handler_user_fsm_feedback
from keyboard.keyboard_handler_user import inline_kb_start_feedback
from lexicon.lexicon_ru import LEXICON_RU_HANDLER

router = Router()
router.include_router(handler_user_fsm_feedback.router)


@router.message(CommandStart())
async def cmd_start(message: Message):
    # Удаляет команду /start после отправки
    await message.delete()

    # Отправляет стартовое сообщение с inline кнопкой, для записи отзыва
    await message.answer(
        text=LEXICON_RU_HANDLER["lexicon_cmd_start"],
        reply_markup=inline_kb_start_feedback,
    )
