from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon_ru import LEXICON_RU_KEYBOARD

inline_kb_start_feedback = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=LEXICON_RU_KEYBOARD["inline_kb_start_feedback"],
                callback_data="write_feedback",
            )
        ]
    ]
)
