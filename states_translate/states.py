from aiogram.fsm.state import State, StatesGroup


class Period(StatesGroup):
    choosing_period = State()
    choosing_office = State()
    choosing_day = State()
    get_mail = State()
    

class Month(StatesGroup):
    choosing_month = State()
