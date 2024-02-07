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
helper = {'yes': "Да", "no": "Нет", "part": "Частично"}


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
