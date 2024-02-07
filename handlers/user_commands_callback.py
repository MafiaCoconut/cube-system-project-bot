import openpyxl
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from icecream import ic

from config.log_def import set_func, set_func_and_person
from keyboards import inline
from handlers import auxiliary
from utils.bot import bot
from utils.states import UserState
from data.text import question_1_1, question_2_1
from config.config import structural_division

tag = "callback_handlers"


async def save_name_callback(call: CallbackQuery, state: FSMContext):
    func_name = "save_name_callback"
    set_func_and_person(func_name, tag, call.message)
    data = await state.get_data()
    name = data['name']
    await state.clear()

    workbook = openpyxl.load_workbook('data/main.xlsx')
    sheet = workbook['Лист1']

    sheet.cell(row=1, column=sheet.max_column+1).value = call.message.chat.id
    sheet.cell(row=2, column=sheet.max_column).value = name

    workbook.save('data/main.xlsx')

    # await call.message.edit_text("Выберите ваше подразделение:",
    #                              reply_markup=inline.get_structural_division())
    await call.answer()


async def rewrite_name_callback(call: CallbackQuery, state: FSMContext):
    func_name = "rewrite_name_callback"
    set_func_and_person(func_name, tag, call.message)

    await call.message.edit_text("Введите ваше ФИО через пробел.")
    await state.set_state(UserState.name)


async def form_division_callback(call: CallbackQuery, state: FSMContext):
    func_name = "form_division_callback"
    set_func_and_person(func_name, tag, call.message)
    await state.clear()
    data = call.data[call.data.find('_')+1:]

    is_montage = False
    text = ""
    match data:
        case "admin":
            text = "Администрация"
        case "project":
            text = "Проектный отдел"
        case "service":
            text = "Сервисный отдел"
        case "montage":
            text = "Отдел монтажа"
            is_montage = True
        case "cmto":
            text = "СМТО"

    auxiliary.save_data(call.message.chat.id, structural_division, text)

    if is_montage:
        await call.message.edit_text(question_2_1, reply_markup=inline.get_question_2_1())
    else:
        await call.message.edit_text(question_1_1, reply_markup=inline.get_question_1_1())



