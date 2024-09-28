from asyncio import run

from database.methods import connect_database
from handler import handler_user
from loader import bot, dispatcher
from utils.logger import logger_main


@dispatcher.startup()
async def on_startup():
    logger_main.info("Бот успешно начал работу")
    try:
        await connect_database()
        logger_main.info("База данных была успешно подключена")
    except BaseException as error:
        logger_main.error(f"Произошла ошибка с подключением к базе данных {error}")


@dispatcher.shutdown()
async def shutdown():
    logger_main.info("Бот успешно прекратил работу")


async def main() -> None:
    dispatcher.include_router(handler_user.router)
    await bot.delete_webhook(drop_pending_updates=True)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    try:
        run(main())
    except KeyboardInterrupt:
        ...
