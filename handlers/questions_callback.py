import pandas as pd
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from icecream import ic

from config.log_def import set_func, set_func_and_person
from keyboards import inline
from handlers import auxiliary
from utils.bot import bot
from data.text import *
from config.config import name, chat_id as chat_id_text, structural_division, \
    question_1, question_2, question_3, question_4

tag = "callback_handlers"
helper = {'1': "Да", "2": "Нет"}


async def menu_sections(call: CallbackQuery, state: FSMContext):
    func_name = "menu_sections"
    set_func_and_person(func_name, tag, call.message)

    # TODO: добавить рядом с названием отдела слово "Пройдено"
    await call.message.edit_text("Выбери раздел, чтобы начать его проходить", reply_markup=inline.get_menu_sections())


async def menu_subsection(call: CallbackQuery, state: FSMContext):
    func_name = "menu_subsection"
    set_func_and_person(func_name, tag, call.message)

    section = call.data[-1]
    match section:
        case "1":
            await call.message.edit_text("Выберите подраздел", reply_markup=inline.get_sections(section, 3))
        case "2":
            await call.message.edit_text("Выберите подраздел", reply_markup=inline.get_sections(section, 3))
        case "3":
            await call.message.edit_text("Выберите подраздел", reply_markup=inline.get_sections(section, 2))
        case "4":
            await call.message.edit_text("Выберите подраздел", reply_markup=inline.get_sections(section, 6))


async def subsection_handler(call: CallbackQuery, state: FSMContext):
    func_name = "subsection_handler"
    set_func_and_person(func_name, tag, call.message)

    header_nummer = call.data[-3:]
    ic(header_nummer)
    if header_nummer == "0.0":
        await menu_sections(call, state)

    else:
        data = await state.get_data()
        data['header_nummer'] = header_nummer
        data['answers'] = []

        header = await call.message.edit_text(auxiliary.get_header(header_nummer))
        data['header_message_id'] = header.message_id

        question = await call.message.answer(
            f"{auxiliary.get_question(data['header_nummer'], len(data['answers']) + 1)}",
            reply_markup=inline.get_questions_options(data['header_nummer']))
        data['main_message_id'] = question.message_id

        ic(data)

        await state.update_data(data)


async def send_question(call: CallbackQuery, state: FSMContext):
    func_name = "send_question"
    set_func_and_person(func_name, tag, call.message)

    data = await state.get_data()

    if len(data['answers']) != auxiliary.headers[data['header_nummer']][1]:
        await call.message.edit_text(
            f"{auxiliary.get_question(data['header_nummer'], len(data['answers']) + 1)}",
            reply_markup=inline.get_questions_options(data['header_nummer']))

    else:
        ic(data)
        auxiliary.save_answers(data['id_in_db'], data['header_nummer'], data['answers'])
        await call.message.edit_text(f"Данные о {data['header_nummer']} сохранены")
        await menu_subsection(call, state)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=data['header_message_id'])

    await call.answer()


async def form_question(call: CallbackQuery, state: FSMContext):
    func_name = "form_question"
    set_func_and_person(func_name, tag, call.message)

    data = await state.get_data()

    data['answers'].append(helper[call.data[-1]])
    ic(data['header_nummer'], data['answers'][-1])

    await state.update_data(data)

    await send_question(call, state)











"""

    # Вывод вопроса
    try:
        text1 = data['header']
        ic(text1)
        text2 = auxiliary.get_question(data['header_nummer'], len(data['answers'])+1)
        ic(text2)
        await call.message.edit_text(f"{data['header']}\n\n{auxiliary.get_question(data['header_nummer'], len(data['answers'])+1)}",
                                     reply_markup=inline.get_questions_options('1.1'))
        ic(len(data['answers']))
        ic(auxiliary.headers[data['header_nummer']][1])
        if len(data['answers']) == auxiliary.headers[data['header']][1]:
            auxiliary.save_answers(call.message.chat.id, data['answers'])
            await call.message.edit_text(f"Данные о {data['header_nummer']} сохранены")
    except Exception as e:
        ic(e)
        data['header'] = auxiliary.get_header('1.1')
        data['header_nummer'] = "1.1"
        data['answers'] = []

        await state.update_data(data)

        await call.message.edit_text(f"{data['header']}\n\n{auxiliary.get_question(data['header_nummer'], len(data['answers'])+1)}",
                                     reply_markup=inline.get_questions_options('1.1'))
    new_data = await state.get_data()
    ic(new_data)

    await call.answer()
    
    """







# async def form_question_1_1(call: CallbackQuery):
#     func_name = "form_question_1_1"
#     set_func_and_person(func_name, tag, call.message)
#
#     data = call.data[13:]
#     text = helper[data]
#     auxiliary.save_data(call.message.chat.id, question_1, text)
#     await call.message.edit_text(text=question_1_2, reply_markup=inline.get_question_1_2())
#
#
# async def form_question_1_2(call: CallbackQuery):
#     func_name = "form_question_1_2"
#     set_func_and_person(func_name, tag, call.message)
#
#     data = call.data[13:]
#
#     text = ""
#     match data:
#         case "answer_1":
#             text = "В основном по указанию непосредственного руководителя"
#         case "answer_2":
#             text = "Как правило, Вы самостоятельно планируете и организовываете свою работу"
#
#     auxiliary.save_data(call.message.chat.id, question_2, text)
#     auxiliary.save_data(call.message.chat.id, question_3, "-")
#     auxiliary.save_data(call.message.chat.id, question_4, "-")
#
#     await call.message.edit_text("Спасибо за прохождение анкеты. Если вы считаете, что вы где-то допустили ошибку, "
#                                  "вы можете пройти анкету ещё раз введя /start")
#
#
# async def form_question_2_1(call: CallbackQuery):
#     func_name = "form_question_2_1"
#     set_func_and_person(func_name, tag, call.message)
#
#     data = call.data[13:]
#     text = helper[data]
#     auxiliary.save_data(call.message.chat.id, question_1, text)
#     await call.message.edit_text(text=question_2_2, reply_markup=inline.get_question_2_2())
#
#
# async def form_question_2_2(call: CallbackQuery):
#     func_name = "form_question_2_2"
#     set_func_and_person(func_name, tag, call.message)
#
#     data = call.data[13:]
#     text = ""
#     match data:
#         case "answer_1":
#             text = "Под руководством непосредственного руководителя (руководителя работ, начальника ОМ, исполнительного директора)"
#         case "answer_2":
#             text = "Вы самостоятельно планируете и организовываете свою работу"
#
#     auxiliary.save_data(call.message.chat.id, question_2, text)
#     await call.message.edit_text(text=question_2_3, reply_markup=inline.get_question_2_3())
#
#
# async def form_question_2_3(call: CallbackQuery):
#     func_name = "form_question_2_3"
#     set_func_and_person(func_name, tag, call.message)
#
#     data = call.data[13:]
#     text = helper[data]
#     auxiliary.save_data(call.message.chat.id, question_3, text)
#     if data == "yes":
#         await call.message.edit_text(text=question_2_4, reply_markup=inline.get_question_2_4())
#     else:
#         await call.message.edit_text("Спасибо за прохождение анкеты. Если вы считаете, что вы где-то допустили ошибку, "
#                                      "вы можете пройти анкету ещё раз введя /start")
#         auxiliary.save_data(call.message.chat.id, question_4, '-')
#
#
# async def form_question_2_4(call: CallbackQuery):
#     func_name = "form_question_2_4"
#     set_func_and_person(func_name, tag, call.message)
#
#     data = call.data[13:]
#     text = ""
#     match data:
#         case "answer_1":
#             text = "В основном под руководством непосредственного руководителя (руководителя работ, начальника ОМ, исполнительного директора)"
#         case "answer_2":
#             text = "Как правило, Вы самостоятельно планируете и организовываете свою работу"
#
#     auxiliary.save_data(call.message.chat.id, question_4, text)
#
#     await call.message.edit_text("Спасибо за прохождение анкеты. Если вы считаете, что вы где-то допустили ошибку, "
#                                  "вы можете пройти анкету ещё раз введя /start")
#
#
