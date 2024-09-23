from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

# from aiogram.fsm.storage.memory import MemoryStorage
from config import settings

dispatcher = Dispatcher()
bot = Bot(
    token=settings.TELEGRAM_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML, protect_content=settings.PROTECT_CONTENT
    ),
)
