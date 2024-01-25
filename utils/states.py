from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    name = State()
    structural_division = State()
    question_1 = State()
    question_2 = State()
    question_3 = State()
    question_4 = State()


class ExampleState(StatesGroup):
    example_state = State()
