import openpyxl
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from utils.logs import set_func_and_person
from handlers.questions_callback import menu_sections
from utils.states import UserState
from utils.postgresql import execute
tag = "callback_handlers"


async def save_name_callback(call: CallbackQuery, state: FSMContext):
    func_name = "save_name_callback"
    set_func_and_person(func_name, tag, call.message)
    data = await state.get_data()
    name = data['name']

    execute(f"INSERT INTO users (telegram_id, telegram_username) VALUES ('{call.message.chat.id}', '{name}')")

    await state.update_data(data)
    await state.set_state()
    await menu_sections(call)
    await call.answer()


async def rewrite_name_callback(call: CallbackQuery, state: FSMContext):
    func_name = "rewrite_name_callback"
    set_func_and_person(func_name, tag, call.message)

    await call.message.edit_text("Введите ваше ФИО через пробел.")
    await state.set_state(UserState.name)
