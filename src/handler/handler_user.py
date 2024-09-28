from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from filter.filter import IsFeedback
from handler import handler_user_fsm_feedback
from keyboard.keyboard_handler_user import inline_kb_start_feedback
from lexicon.lexicon_ru import LEXICON_RU_HANDLER
from utils.logger import logger_handler_user

router = Router()
router.include_router(handler_user_fsm_feedback.router)


@router.message(CommandStart(), ~IsFeedback())
async def cmd_start_feedback_false(message: Message):
    logger_handler_user.info(
        f"User ID = {message.from_user.id} выполнил команду /start ~"
    )
    # Удаляет команду /start после отправки команды
    await message.delete()

    # Отправляет стартовое сообщение с inline кнопкой, для записи отзыва
    await message.answer(
        text=LEXICON_RU_HANDLER["cmd_start_feedback_false"],
        reply_markup=inline_kb_start_feedback,
    )
    logger_handler_user.info(
        f"User ID = {message.from_user.id} успешно получил стартовое сообщение"
    )


@router.message(CommandStart(), IsFeedback())
async def cmd_start_feedback_true(message: Message):
    logger_handler_user.info(
        f"User ID = {message.from_user.id} выполнил команду /start"
    )
    # Удаляет команду /start после отправки команды
    await message.delete()
    await message.answer(text=LEXICON_RU_HANDLER["cmd_start_feedback_true"])
    logger_handler_user.info(
        f"User ID = {message.from_user.id} успешно получил сообщение"
    )
