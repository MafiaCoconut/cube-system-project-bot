from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)


def get_question_1_1():
    question_1_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data='question_1_1_yes'),
             InlineKeyboardButton(text="2", callback_data='question_1_1_part'),
             InlineKeyboardButton(text="3", callback_data='question_1_1_no')],
        ]
    )
    return question_1_1


def get_question_1_2():
    question_1_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data='question_1_2_answer_1'),
             InlineKeyboardButton(text="2", callback_data='question_1_2_answer_2')],
        ]
    )
    return question_1_2


def get_question_2_1():
    question_2_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data='question_2_1_yes'),
             InlineKeyboardButton(text="2", callback_data='question_2_1_part'),
             InlineKeyboardButton(text="3", callback_data='question_2_1_no')],
        ]
    )
    return question_2_1


def get_question_2_2():
    question_2_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data='question_2_2_answer_1'),
             InlineKeyboardButton(text="2", callback_data='question_2_2_answer_2')]
        ]
    )
    return question_2_2


def get_question_2_3():
    question_2_3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data='question_2_3_yes'),
             InlineKeyboardButton(text="2", callback_data='question_2_3_no')],
        ]
    )
    return question_2_3


def get_question_2_4():
    question_2_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data='question_2_4_answer_1'),

             InlineKeyboardButton(text="2", callback_data='question_2_4_answer_2')],
        ]
    )
    return question_2_4
