from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile
from aiogram.fsm.context import FSMContext
from icecream import ic

from handlers import auxiliary
from keyboards import inline

from utils.logs import set_func, set_func_and_person
from utils.states import UserState
from utils.bot import bot
from filters.is_admin import IsAdmin

router = Router()
tag = "user_commands"
status = "debug"
file_path = 'data/main.xlsx'


@router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    function_name = "command_start_handler"
    set_func(function_name, tag, status)

    msg = await message.answer("Добро пожаловать!\nВведите ваше ФИО через пробел.")
    await state.set_state(UserState.name)
    await state.update_data(main_message_id=msg.message_id)

    # is_exist = auxiliary.is_exist(message.chat.id)
    # if is_exist == -1:
    #     msg = await message.answer("Добро пожаловать!\nВведите ваше ФИО через пробел.")
    #     await state.set_state(UserState.name)
    #     await state.update_data(main_message_id=msg.message_id)
    # else:
    #     await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@router.message(UserState.name)
async def form_name_handler(message: Message, state: FSMContext) -> None:
    function_name = "form_name_handler"
    set_func_and_person(function_name, tag, message)

    fio = message.text.split(' ')
    data = await state.get_data()

    if len(fio) != 3:
        try:
            await bot.edit_message_text(chat_id=message.chat.id, message_id=data["main_message_id"],
                                        text="Неправильный формат. Повторите попытку.")
        except:
            pass
    else:
        text = f"Проверьте правильность введённых данных\n\n{message.text}"

        await state.update_data(name=message.text)

        await bot.edit_message_text(chat_id=message.chat.id, message_id=data["main_message_id"],
                                    text=text, reply_markup=inline.get_save_or_recreate())
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


@router.message(Command('send_data'), IsAdmin())
async def send_data(message: Message):
    function_name = "form_name_handler"
    set_func_and_person(function_name, tag, message)

    for i in range(1, 5):
        await message.answer_document(document=FSInputFile(path=f'data/section_{i}.xlsx'))


@router.message(F.text == '/send_user_logs', IsAdmin())
async def admin_send_user_logs_with_command(message: Message):
    function_name = "admin_send_user_logs_with_command"
    set_func(function_name, tag)

    text = "Пользовательские логи отправлены"

    await message.answer_document(text=text, document=FSInputFile(path='user_data.log'))


@router.message(F.text == '/send_system_logs', IsAdmin())
async def admin_send_system_logs_with_command(message: Message):
    function_name = "admin_send_system_logs_with_command"
    set_func(function_name, tag)

    text = "Логи отправлены"

    await message.answer_document(text=text, document=FSInputFile(path='system_data.log'))


@router.message(Command('main_menu'))
async def main_menu_handler(message: Message):
    function_name = "main_menu_handler"
    set_func_and_person(function_name, tag, message)

    await message.answer("Выбери раздел, чтобы начать его проходить", reply_markup=inline.get_menu_sections())


from utils.postgresql import cur


@router.message(Command('get_test'))
async def admin_get_headers(message: Message):
    function_name = "admin_get_headers"
    set_func(function_name, tag)

    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    ic(data)
    ic(type(data))
    await message.answer(str(data))
