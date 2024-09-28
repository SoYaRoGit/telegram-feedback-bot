from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from database.methods import create_feedback
from keyboard.keyboard_handler_user import (
    inline_kb_cancel_feedback,
    inline_kb_confirm_feedback,
)
from lexicon.lexicon_ru import LEXICON_RU_HANDLER
from loader import bot
from state.state import FeedBackState
from utils.logger import handler_user_fsm_feedback

router = Router()


@router.callback_query(F.data.in_("write_feedback"))
async def start_write_feedback(callback: CallbackQuery, state: FSMContext):
    handler_user_fsm_feedback.info(
        f"User ID = {callback.message.from_user.id} callback запрос на создание отзыва"
    )
    # Очищаем FSM
    await state.clear()

    await callback.message.edit_text(
        LEXICON_RU_HANDLER["start_write_feedback"],
        reply_markup=inline_kb_cancel_feedback,
    )

    # Устанавливаем состояние ввода отзыва
    await state.set_state(FeedBackState.TEXT)
    handler_user_fsm_feedback.info(
        f"User ID = {callback.message.from_user.id} перешёл на FSM состояние TEXT"
    )

    # Сохраняем сообщние для дальнейшего обновления
    await state.update_data(message_id=callback.message.message_id)

    await callback.answer()


@router.message(StateFilter(FeedBackState.TEXT))
async def fsm_feedback_text(message: Message, state: FSMContext):
    # Удалить введенный пользователем отзыв
    await message.delete()

    feedback = message.text.strip()
    # Сохранить в FSM введенный текст
    await state.update_data(text=feedback)
    handler_user_fsm_feedback.info(
        f"User ID = {message.from_user.id} успешно ввёл текст {feedback}"
    )

    # Получаем данные из FSM
    data: dict = await state.get_data()

    # Обновляем сообщение
    await bot.edit_message_text(
        text=LEXICON_RU_HANDLER["fsm_feedback_text"].format(
            message.from_user.full_name, data["text"]
        ),
        chat_id=message.chat.id,
        message_id=data["message_id"],
        reply_markup=inline_kb_confirm_feedback,
    )
    handler_user_fsm_feedback.info(
        f"User ID = {message.from_user.id} предложен выбор сохранить или удалить отзыв"
    )


@router.callback_query(F.data.in_("cancel_feedback"))
async def fsm_feedback_cancel(callback: CallbackQuery, state: FSMContext):
    # Очищаем FSM
    await state.clear()

    # Удаляю сообщение
    await callback.message.delete()

    await callback.answer()
    handler_user_fsm_feedback.info(
        f"User ID = {callback.message.from_user.id} отменил отзыв"
    )


@router.callback_query(F.data.in_("save_feedback"))
async def fsm_feedback_save(callback: CallbackQuery, state: FSMContext):
    data: dict = await state.get_data()

    # Очищаем FSM
    await state.clear()

    try:
        await create_feedback(
            user_id=callback.from_user.id,
            user_name=callback.from_user.full_name,
            text=data["text"],
        )
        handler_user_fsm_feedback.info(
            f"User ID = {callback.message.from_user.id} отзыв успешно сохранен в БЛ"
        )

    except BaseException:
        handler_user_fsm_feedback.warning(
            f"User ID = {callback.message.from_user.id} произошла ошибка при сохранении отзыва"
        )
    # Выводим информацию, что отзыв был сохранен
    await callback.answer(text=LEXICON_RU_HANDLER["fsm_feedback_save"])

    # Удаляем
    await callback.message.delete()
    handler_user_fsm_feedback.warning(
        f"User ID = {callback.message.from_user.id} успешно завершен процесс создания отзыв"
    )
