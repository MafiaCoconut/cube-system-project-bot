from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Начать прохождение анкеты'
        ),
        BotCommand(
            command='main_menu',
            description='Вывести главное меню'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())