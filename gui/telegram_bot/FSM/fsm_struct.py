from aiogram.fsm.state import StatesGroup, State


class FSMFillVacancy(StatesGroup):
    fill_title = State()
    fill_exp = State()
    fill_format = State()
    fill_employment = State()
    fill_schedule = State()
    fill_hours = State()
    fill_city = State()
    fill_payments = State()
    fill_detailed_info = State()
    fill_skills = State()
    fill_confirmation = State()