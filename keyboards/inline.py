from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from fluent.runtime import FluentLocalization


def get_main_menu():
    main_menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='main-menu', callback_data="menu_main")]]
    )
    return main_menu


def get_go_to(where):
    go_to = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='back', callback_data=f"menu_{where}"),
             InlineKeyboardButton(text='to-menu-main', callback_data="menu_main")]
        ]
    )
    return go_to


def get_settings_language_from_start():
    languages = get_main_menu()
    menu_main = get_go_to("main")
    languages.inline_keyboard.append(menu_main.inline_keyboard[0])

    return languages


def get_check_or_recreate():
    check_or_recreate = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Сохранить", callback_data='fio_save')],
            [InlineKeyboardButton(text="Перезаписать", callback_data='fio_rewrite')]
        ]
    )
    return check_or_recreate


def get_structural_division():
    structural_division = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Администрация", callback_data="division_admin")],
            [InlineKeyboardButton(text="Проектный отдел", callback_data="division_project")],
            [InlineKeyboardButton(text="Сервисный отдел", callback_data="division_service")],
            [InlineKeyboardButton(text="Отдел монтажа", callback_data="division_montage")],
            [InlineKeyboardButton(text="СМТО", callback_data="division_cmto")]
        ]
    )
    return structural_division


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
            [InlineKeyboardButton(text="1", callback_data='question_2_3_yes')],
            [InlineKeyboardButton(text="2", callback_data='question_2_3_no')],
        ]
    )
    return question_2_3


def get_question_2_4():
    question_2_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="1", callback_data='question_2_4_answer_1')],

            [InlineKeyboardButton(text="2", callback_data='question_2_4_answer_2')],
        ]
    )
    return question_2_4
