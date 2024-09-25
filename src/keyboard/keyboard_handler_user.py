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


inline_kb_cancel_feedback = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=LEXICON_RU_KEYBOARD["inline_kb_cancel_feedback"],
                callback_data="cancel_feedback",
            )
        ]
    ]
)


inline_kb_confirm_feedback = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text=LEXICON_RU_KEYBOARD["inline_kb_confirm_feedback"]["cancel"],
                callback_data="cancel_feedback",
            )
        ],
        [
            InlineKeyboardButton(
                text=LEXICON_RU_KEYBOARD["inline_kb_confirm_feedback"]["save"],
                callback_data="save_feedback",
            )
        ],
    ]
)
