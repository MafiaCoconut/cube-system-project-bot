import asyncio


from app.utils import registration_dispatcher, commands

from app.config_reader import get_token
from app.utils.logs import logs_settings
from app.utils.bot import bot


async def main() -> None:
    registration_dispatcher.include_routers()
    registration_dispatcher.register_all_callbacks()

    await commands.set_commands(bot)
    await registration_dispatcher.dp.start_polling(bot)


if __name__ == "__main__":
    logs_settings()
    asyncio.run(main())
