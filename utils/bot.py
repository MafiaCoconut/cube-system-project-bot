from aiogram import Bot
from aiogram.enums import ParseMode

from config.config import get_token
TOKEN = get_token()


bot = Bot(TOKEN, parse_mode=ParseMode.HTML)