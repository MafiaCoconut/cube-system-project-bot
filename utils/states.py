from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    last_message_id = State()
    id_in_db = State
    name = State()
    header = State()
    header_nummer = State()
    answers = State()



class ExampleState(StatesGroup):
    example_state = State()
