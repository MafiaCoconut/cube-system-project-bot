import asyncio

from app.utils import registration_dispatcher, commands

from app.config import get_token
from app.config import settings
from app.utils.bot import bot

TOKEN = get_token()


async def main() -> None:
    registration_dispatcher.include_routers()
    registration_dispatcher.register_all_callbacks()

    await commands.set_commands(bot)
    await registration_dispatcher.dp.start_polling(bot)


if __name__ == "__main__":
    settings.main()
    asyncio.run(main())
