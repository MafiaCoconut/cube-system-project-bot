import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from handlers import auxiliary
from keyboards import inline

import pandas as pd
import openpyxl
from icecream import ic

from config.log_def import set_func, set_func_and_person
from utils.fluent import list_of_available_languages
from utils.states import UserState
from utils.bot import bot
from config.config import name
from filters.is_admin import IsAdmin
router = Router()
tag = "user_commands"
status = "debug"
file_path = 'data/main.xlsx'


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_start_handler"
    set_func(function_name, tag, status)

    msg = await message.answer("Добро пожаловать!\nВведите ваше ФИО через пробел.")

    # workbook = openpyxl.load_workbook('data/main.xlsx')
    # ic(workbook.sheetnames)

    # df = pd.read_excel(file_path).astype('str')

    # Проверка существует ли человек в базе данных
    # row_index = df[df["ID"] == str(message.chat.id)].index.tolist()
    # ic(row_index)

    # if not row_index:
    #     Если не существует, то добавляется в бд
        # df.loc[len(df), "ID"] = str(message.chat.id)
        # df.to_excel(file_path, index=False)

    # ic(df)
    await state.set_state(UserState.name)
    await state.update_data(last_message_id=msg.message_id)


@router.message(UserState.name)
async def form_name_handler(message: Message, state: FSMContext) -> None:
    function_name = "form_name_handler"
    set_func_and_person(function_name, tag, message)

    fio = message.text.split(' ')
    data = await state.get_data()

    if len(fio) != 3:
        await bot.edit_message_text(chat_id=message.chat.id, message_id=data["last_message_id"],
                                    text="Неправильный формат. Повторите попытку.")
    else:
        # auxiliary.save_data(message.chat.id, name, message.text)
        text = f"Проверьте правильность введённых данных\n\n{message.text}"

        await state.update_data(name=message.text)

        await bot.edit_message_text(chat_id=message.chat.id, message_id=data["last_message_id"],
                                    text=text, reply_markup=inline.get_save_or_recreate())
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@router.message(Command('send_data'), IsAdmin())
async def send_data(message: Message):
    function_name = "form_name_handler"
    set_func_and_person(function_name, tag, message)

    await message.answer_document(document=FSInputFile(path='data/main.xlsx'))


@router.message(Command('send_logs'), IsAdmin())
async def admin_send_logs_with_command(message: Message):
    function_name = "admin_send_logs_with_command"
    set_func(function_name, tag)

    text = "Логи отправлены"

    await message.answer_document(text=text, document=FSInputFile(path='data.log'))

