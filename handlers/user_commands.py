import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from handlers import auxiliary
from keyboards import inline

import pandas as pd

from config.log_def import set_func, set_func_and_person
from utils.fluent import list_of_available_languages
from utils.states import UserState
from config.config import name, chat_id as chat_id_text, structural_division, \
    question_1, question_2, question_3, question_4

router = Router()
tag = "user_commands"
status = "debug"
file_path = 'data/main.xlsx'


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_start_handler"
    set_func(function_name, tag, status)

    await message.answer("Добро пожаловать!\nВведите ваше ФИО через пробел.")

    df = pd.read_excel(file_path)
    print(df)
    row_index = df.index[df['ID'] == message.chat.id].tolist()
    if not row_index:

        first_empty_cell = df["ID"].isna().idxmax() if df["ID"].isna().any() else len(df)

        if first_empty_cell == len(df):
            df.loc[first_empty_cell] = [str(message.chat.id)] + [pd.NA] * (len(df.columns) - 1)
        else:
            df.at[first_empty_cell, "ID"] = message.chat.id

        df.to_excel(file_path, index=False)

    await state.set_state(UserState.name)


@router.message(UserState.name)
async def form_name_handler(message: Message, state: FSMContext) -> None:
    function_name = "form_name_handler"
    set_func_and_person(function_name, tag, message)

    fio = message.text.split(' ')

    if len(fio) != 3:
        await message.answer("Неправильный формат. Повторите попытку.")
    else:
        df = pd.read_excel('data/main.xlsx')
        row_index = df.index[df['ID'] == message.chat.id].tolist()[0]
        df.at[row_index, name] = message.text
        print(df)
        df.to_excel(file_path, index=False)




