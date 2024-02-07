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


def get_save_or_recreate():
    save_or_recreate = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Сохранить", callback_data='fio_save')],
            [InlineKeyboardButton(text="Перезаписать", callback_data='fio_rewrite')]
        ]
    )
    return save_or_recreate


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


def get_questions_options(questions_number):
    questions_number