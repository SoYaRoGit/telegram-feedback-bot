from asyncio import run

from database.methods import connect_database
from handler import handler_user
from loader import bot, dispatcher


@dispatcher.startup()
async def on_startup():
    await connect_database()
    print("Бот включён")


@dispatcher.shutdown()
async def shutdown():
    print("Бот отключён")


async def main() -> None:
    dispatcher.include_router(handler_user.router)
    await bot.delete_webhook(drop_pending_updates=True)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    try:
        run(main())
    except KeyboardInterrupt:
        ...
