import asyncio

from utils import commands, registration_dispatcher

from config.config import get_token
from config import settings
from utils.bot import bot

TOKEN = get_token()


async def main() -> None:
    registration_dispatcher.include_routers()

    await commands.set_commands(bot)
    await registration_dispatcher.dp.start_polling(bot)


if __name__ == "__main__":
    settings.main()
    asyncio.run(main())
