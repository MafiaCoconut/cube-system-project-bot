from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from app.config import send_log
from app.utils.bot import bot
from app.handlers import user_commands, auxiliary
from icecream import ic


tag = "bot_messages"
router = Router()


@router.message()
# @router.message(F.content_type.in_({'sticker'}))
async def echo_handler(message: Message, state: FSMContext) -> None:
    """Функция вывода заглушки на необъявленное сообщение/команду"""

    is_exist = auxiliary.is_exist(message.chat.id)
    ic(is_exist)
    if is_exist != -1:
        send_log(message.text, message.chat.username)
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    else:
        await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
        await user_commands.command_start_handler(message, state)


    # await message.answer("Команды не найдено. Повторите попытку ввода.")



