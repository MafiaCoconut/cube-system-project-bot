from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from app.utils.logs import set_func_and_person
from app.keyboards import inline
from app.handlers import auxiliary
from app.utils.bot import bot

tag = "callback_handlers"
helper = {'1': "Да", "2": "Нет"}


async def menu_sections(call: CallbackQuery):
    func_name = "menu_sections"
    set_func_and_person(func_name, tag, call.message)

    await call.message.edit_text("Выбери раздел, чтобы начать его проходить", reply_markup=inline.get_menu_sections())


async def menu_subsection(call: CallbackQuery, state: FSMContext, status=0):
    func_name = "menu_subsection"
    set_func_and_person(func_name, tag, call.message)

    data = await state.get_data()

    if status == 1:
        section = data['header_nummer'][0]
        text = "Ваши ответы успешно сохранены\n\nВыберите подраздел"
    else:
        text = "Выберите подраздел"
        section = call.data[-1]
    sections = [3, 3, 2, 6]  # количество подразделов в разделах 1, 2, 3, 4

    await call.message.edit_text(text, reply_markup=inline.get_sections(
                                       auxiliary.get_id_in_db(call.message.chat.id),
                                       section,
                                       sections[int(section)-1]))


async def subsection_handler(call: CallbackQuery, state: FSMContext):
    func_name = "subsection_handler"
    set_func_and_person(func_name, tag, call.message)

    header_nummer = call.data[-3:]
    if header_nummer == "0.0":
        await menu_sections(call, state)

    else:
        data = await state.get_data()
        data['header_nummer'] = header_nummer
        data['answers'] = []

        header = await call.message.edit_text(auxiliary.get_header(header_nummer))
        data['header_message_id'] = header.message_id

        question = await call.message.answer(
            f"Обладаете ли вы этим умением?\n\n{auxiliary.get_question(data['header_nummer'], len(data['answers']) + 1)}",
            reply_markup=inline.get_questions_options(data['header_nummer']))
        data['main_message_id'] = question.message_id

        await state.update_data(data)


async def send_question(call: CallbackQuery, state: FSMContext):
    func_name = "send_question"
    set_func_and_person(func_name, tag, call.message)

    data = await state.get_data()

    if len(data['answers']) != auxiliary.headers[data['header_nummer']][1]:
        if len(data['answers'])+1 < auxiliary.headers[data['header_nummer']][2]:
            text = "Обладаете ли вы этим умением?\n\n"
        else:
            text = "Владеете ли вы этим знанием?\n\n"
        await call.message.edit_text(
            f"{text}{auxiliary.get_question(data['header_nummer'], len(data['answers']) + 1)}",
            reply_markup=inline.get_questions_options(data['header_nummer']))

    else:
        auxiliary.save_answers(auxiliary.get_id_in_db(call.message.chat.id), data['header_nummer'], data['answers'])
        await menu_subsection(call, state, 1)
        await bot.delete_message(chat_id=call.message.chat.id, message_id=data['header_message_id'])

    await call.answer()


async def form_question(call: CallbackQuery, state: FSMContext):
    func_name = "form_question"
    set_func_and_person(func_name, tag, call.message)

    data = await state.get_data()

    data['answers'].append(helper[call.data[-1]])

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




