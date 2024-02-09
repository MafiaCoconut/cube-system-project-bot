import openpyxl
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from config.log_def import set_func, set_func_and_person
from handlers.questions_callback import menu_sections
from keyboards import inline
from handlers import auxiliary
from utils.bot import bot
from utils.states import UserState

tag = "callback_handlers"


async def save_name_callback(call: CallbackQuery, state: FSMContext):
    func_name = "save_name_callback"
    set_func_and_person(func_name, tag, call.message)
    data = await state.get_data()
    name = data['name']

    workbook_persons = openpyxl.load_workbook('data/persons.xlsx')
    sheet = workbook_persons['Лист1']
    is_exist = auxiliary.is_exist(call.message.chat.id)

    if is_exist == -1:
        sheet.cell(row=1, column=sheet.max_column+1).value = call.message.chat.id
        sheet.cell(row=2, column=sheet.max_column).value = name

        for i in range(1, 5):
            workbook = openpyxl.load_workbook(f'data/section_{i}.xlsx')
            sheet = workbook['Лист1']
            sheet.cell(row=1, column=sheet.max_column + 1).value = call.message.chat.id
            sheet.cell(row=2, column=sheet.max_column).value = name
            workbook.save(f'data/section_{i}.xlsx')

    else:
        sheet.cell(row=2, column=is_exist).value = name

    await state.update_data(data)

    workbook_persons.save('data/persons.xlsx')
    await menu_sections(call, state)
    await call.answer()


async def rewrite_name_callback(call: CallbackQuery, state: FSMContext):
    func_name = "rewrite_name_callback"
    set_func_and_person(func_name, tag, call.message)

    await call.message.edit_text("Введите ваше ФИО через пробел.")
    await state.set_state(UserState.name)
