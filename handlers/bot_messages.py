from aiogram import Router, types, F
from aiogram.types import Message

from config.log_def import set_inside_func, send_log
from utils.bot import bot
from handlers import auxiliary
from keyboards import reply, inline


tag = "bot_messages"
router = Router()


@router.message()
# @router.message(F.content_type.in_({'sticker'}))
async def echo_handler(message: Message) -> None:
    """Функция вывода заглушки на необъявленное сообщение/команду"""
    send_log(message.text, message.chat.username)
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    # await message.answer("Команды не найдено. Повторите попытку ввода.")



