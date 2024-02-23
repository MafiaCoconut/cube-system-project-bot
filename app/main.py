import asyncio

from utils import registration_dispatcher, commands
from utils.logs import logs_settings, system_logger
from utils.bot import bot
from utils.postgresql import close_connection, create_table


async def main() -> None:
    try:
        registration_dispatcher.include_routers()
        registration_dispatcher.register_all_callbacks()
        create_table()
        await commands.set_commands(bot)
        await registration_dispatcher.dp.start_polling(bot)
    except Exception as e:
        system_logger.error(e)
    finally:
        close_connection()


if __name__ == "__main__":
    logs_settings()
    asyncio.run(main())
