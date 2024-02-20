from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery
from app.config_reader import get_admin_id


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return str(message.chat.id) in get_admin_id().split(' ')


class IsAdminCallback(BaseFilter):
    async def __call__(self, call: CallbackQuery) -> bool:
        return str(call.message.chat.id) == get_admin_id()

