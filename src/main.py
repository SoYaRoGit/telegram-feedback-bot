from asyncio import run

from loader import bot, dispatcher


@dispatcher.startup()
async def on_startup():
    print("Бот включён")


@dispatcher.shutdown()
async def shutdown():
    print("Бот отключён")


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    try:
        run(main())
    except KeyboardInterrupt:
        ...
