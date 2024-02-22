from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from handlers import auxiliary


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
    questions_numbers = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Да", callback_data=f"question_{questions_number}_1"),
             InlineKeyboardButton(text="Нет", callback_data=f"question_{questions_number}_2")]
        ]
    )
    return questions_numbers


def get_menu_sections():
    menu_sections = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Раздел 1", callback_data="sections_1")],
            [InlineKeyboardButton(text="Раздел 2", callback_data="sections_2")],
            [InlineKeyboardButton(text="Раздел 3", callback_data="sections_3")],
            [InlineKeyboardButton(text="Раздел 4", callback_data="sections_4")],
        ]
    )
    return menu_sections


def get_sections(id_in_db: str, main_section: str, max_sections: int):
    ls = []
    for i in range(1, max_sections+1):
        ls.append([InlineKeyboardButton(text=f"Раздел {main_section}.{i} {auxiliary.get_status_section(id_in_db, f'{main_section}.{i}')}",
                                        callback_data=f"subsection_{main_section}.{i}")])
    ls.append([InlineKeyboardButton(text="Назад", callback_data="subsection_0.0")])

    sections = InlineKeyboardMarkup(inline_keyboard=ls)
    return sections

