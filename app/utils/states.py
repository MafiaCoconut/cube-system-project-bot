from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    header_message_id = State()  # Id сообщения с заголовком
    main_message_id = State()  # Id основного сообщения, в котором происходит взаимодействие
    id_in_db = State  # Id столбца в excel таблице
    name = State()  # ФИО пользователя
    header = State()  # Текущий заголовок
    header_nummer = State()  # Номер текущего заголовка
    answers = State()  # Ответы на текущий заголовок


class ExampleState(StatesGroup):
    example_state = State()
