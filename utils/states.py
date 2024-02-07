from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    last_message_id = State()
    name = State()


class ExampleState(StatesGroup):
    example_state = State()
