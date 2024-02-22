import asyncio

from app.utils import registration_dispatcher, commands
from app.utils.logs import logs_settings, system_logger
from app.utils.bot import bot
from app.utils.postgresql import close_connection


async def main() -> None:
    try:
        registration_dispatcher.include_routers()
        registration_dispatcher.register_all_callbacks()

        await commands.set_commands(bot)
        await registration_dispatcher.dp.start_polling(bot)
    except Exception as e:
        system_logger.error(e)
    finally:
        close_connection()


if __name__ == "__main__":
    logs_settings()
    asyncio.run(main())
