import logging

from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from handlers import auxiliary
from keyboards import inline

from config.log_def import set_func, set_func_and_person
from utils.fluent import list_of_available_languages

router = Router()
tag = "user_commands"
status = "debug"


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_start_handler"
    set_func(function_name, tag, status)

    await message.answer("Добро пожаловать!")


@router.message(Command("help"))
async def command_help_handler(message: Message, state: FSMContext) -> None:
    function_name = "main_menu_handler"
    set_func_and_person(function_name, tag, message)

    await message.answer("Вывод help информации")
