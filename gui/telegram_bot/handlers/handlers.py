from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state

from gui.telegram_bot.FSM.fsm_struct import FSMFillVacancy
from gui.telegram_bot.keyboards.keyboards import (keyboard_exp, keyboard_format, keyboard_employment, keyboard_schedule,
                                                  keyboard_hours, keyboard_cities, keyboard_payments, keyboard_skip,
                                                  keyboard_choice_salary)
from gui.telegram_bot.utils_tg import tg_generate_vacancy_data_for_endpoint_request

router = Router()


@router.message(Command('start'))
async def process_start_command(message: Message):
    await message.answer(
        text='Привет\n\n'
             'Это телеграм-бот, который предскажет примерную з/п вакансии, связанной с IT\n\n'
             'Чтобы перейти к заполнению анкеты - '
             'отправьте команду /fillvacancy'
    )


@router.message(Command(commands='cancel'), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(
        text='Отменять нечего. Вы вне машины состояний\n\n'
             'Чтобы перейти к заполнению анкеты - '
             'отправьте команду /fillvacancy'
    )


@router.message(Command(commands='cancel'), ~StateFilter(default_state))
async def process_cancel_inside(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text='Заполнение отменено. Все данные очищены.\n\n'
             'Чтобы начать заново - отправьте /fillvacancy'
    )


@router.message(Command(commands='fillvacancy'), StateFilter(default_state))
async def process_fill_vacancy_data_command(message: Message, state: FSMContext):
    await state.set_state(FSMFillVacancy.fill_title)
    await message.answer(text="Введите название вакансии")


@router.message(StateFilter(FSMFillVacancy.fill_title))
async def process_title_sent(message: Message, state: FSMContext):
    await state.update_data(title=message.text)
    await state.set_state(FSMFillVacancy.fill_exp)
    await message.answer(text="Выберите опыт требуемый для вакансии", reply_markup=keyboard_exp)


@router.callback_query(F.data == 'btn_no_exp')
async def process_btn_no_exp_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(experience="Нет опыта")
    await state.set_state(FSMFillVacancy.fill_format)
    await callback.message.edit_text(text="Выберите формат работы", reply_markup=keyboard_format)
    await callback.answer()


@router.callback_query(F.data == 'btn_junior_exp')
async def process_btn_junior_exp_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(experience="1-3 года")
    await state.set_state(FSMFillVacancy.fill_format)
    await callback.message.edit_text(text="Выберите формат работы", reply_markup=keyboard_format)
    await callback.answer()


@router.callback_query(F.data == 'btn_middle_exp')
async def process_btn_middle_exp_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(experience="3-6 лет")
    await state.set_state(FSMFillVacancy.fill_format)
    await callback.message.edit_text(text="Выберите формат работы", reply_markup=keyboard_format)
    await callback.answer()


@router.callback_query(F.data == 'btn_senior_exp')
async def process_btn_senior_exp_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(experience="6+ лет")
    await state.set_state(FSMFillVacancy.fill_format)
    await callback.message.edit_text(text="Выберите формат работы", reply_markup=keyboard_format)
    await callback.answer()


@router.callback_query(F.data == 'btn_office_format')
async def process_btn_office_format_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_format="Офис")
    await state.set_state(FSMFillVacancy.fill_employment)
    await callback.message.edit_text(text="Выберите тип занятости", reply_markup=keyboard_employment)
    await callback.answer()


@router.callback_query(F.data == 'btn_remote_format')
async def process_btn_remote_format_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_format="Удалённо")
    await state.set_state(FSMFillVacancy.fill_employment)
    await callback.message.edit_text(text="Выберите тип занятости", reply_markup=keyboard_employment)
    await callback.answer()


@router.callback_query(F.data == 'btn_hybrid_format')
async def process_btn_hybrid_format_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_format="Гибрид")
    await state.set_state(FSMFillVacancy.fill_employment)
    await callback.message.edit_text(text="Выберите тип занятости", reply_markup=keyboard_employment)
    await callback.answer()


@router.callback_query(F.data == 'btn_no_format')
async def process_btn_no_format_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_format="Не указано")
    await state.set_state(FSMFillVacancy.fill_employment)
    await callback.message.edit_text(text="Выберите тип занятости", reply_markup=keyboard_employment)
    await callback.answer()


@router.callback_query(F.data == 'btn_full_employment')
async def process_btn_full_employment_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(common_employment='Полная занятость')
    await state.set_state(FSMFillVacancy.fill_schedule)
    await callback.message.edit_text(text="Укажите график работы", reply_markup=keyboard_schedule)
    await callback.answer()


@router.callback_query(F.data == 'btn_part_employment')
async def process_btn_part_employment_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(common_employment='Частичная занятость')
    await state.set_state(FSMFillVacancy.fill_schedule)
    await callback.message.edit_text(text="Укажите график работы", reply_markup=keyboard_schedule)
    await callback.answer()


@router.callback_query(F.data == 'btn_intern_employment')
async def process_btn_intern_employment_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(common_employment='Стажировка/Проект')
    await state.set_state(FSMFillVacancy.fill_schedule)
    await callback.message.edit_text(text="Укажите график работы", reply_markup=keyboard_schedule)
    await callback.answer()


@router.callback_query(F.data == 'btn_classic_schedule')
async def process_btn_classic_schedule_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_schedule='Классический (5/2)')
    await state.set_state(FSMFillVacancy.fill_hours)
    await callback.message.edit_text(text="Выберите количество рабочих часов", reply_markup=keyboard_hours)
    await callback.answer()


@router.callback_query(F.data == 'btn_free_schedule')
async def process_btn_free_schedule_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_schedule='Свободный')
    await state.set_state(FSMFillVacancy.fill_hours)
    await callback.message.edit_text(text="Выберите количество рабочих часов", reply_markup=keyboard_hours)
    await callback.answer()


@router.callback_query(F.data == 'btn_other_schedule')
async def process_btn_other_schedule_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_schedule='Другие')
    await state.set_state(FSMFillVacancy.fill_hours)
    await callback.message.edit_text(text="Выберите количество рабочих часов", reply_markup=keyboard_hours)
    await callback.answer()


@router.callback_query(F.data == 'btn_no_schedule')
async def process_btn_no_schedule_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_schedule='Не указано')
    await state.set_state(FSMFillVacancy.fill_hours)
    await callback.message.edit_text(text="Выберите количество рабочих часов", reply_markup=keyboard_hours)
    await callback.answer()


@router.callback_query(F.data == 'btn_eight_hours')
async def process_btn_eight_hours_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_hours='8 часов')
    await state.set_state(FSMFillVacancy.fill_city)
    await callback.message.edit_text(text="Укажите город", reply_markup=keyboard_cities)
    await callback.answer()


@router.callback_query(F.data == 'btn_twelve_hours')
async def process_btn_twelve_hours_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_hours='12 часов')
    await state.set_state(FSMFillVacancy.fill_city)
    await callback.message.edit_text(text="Укажите город", reply_markup=keyboard_cities)
    await callback.answer()


@router.callback_query(F.data == 'btn_six_hours')
async def process_btn_six_hours_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_hours='6 часов')
    await state.set_state(FSMFillVacancy.fill_city)
    await callback.message.edit_text(text="Укажите город", reply_markup=keyboard_cities)
    await callback.answer()


@router.callback_query(F.data == 'btn_agree_hours')
async def process_btn_agree_hours_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_hours='По договоренности')
    await state.set_state(FSMFillVacancy.fill_city)
    await callback.message.edit_text(text="Укажите город", reply_markup=keyboard_cities)
    await callback.answer()


@router.callback_query(F.data == 'btn_other_hours')
async def process_btn_other_hours_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_hours='Другие')
    await state.set_state(FSMFillVacancy.fill_city)
    await callback.message.edit_text(text="Укажите город", reply_markup=keyboard_cities)
    await callback.answer()


@router.callback_query(F.data == 'btn_no_hours')
async def process_btn_no_hours_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(work_hours='Не указано')
    await state.set_state(FSMFillVacancy.fill_city)
    await callback.message.edit_text(text="Укажите город", reply_markup=keyboard_cities)
    await callback.answer()


@router.callback_query(F.data == 'btn_moscow')
async def process_btn_moscow_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Moscow')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_spb')
async def process_btn_spb_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='SPB')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_ekb')
async def process_btn_ekb_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Ekaterinburg')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_novosibirsk')
async def process_btn_novosibirsk_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Novosibirsk')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_vladivostok')
async def process_btn_vladivostok_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Vladivostok')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_volgograd')
async def process_btn_volgograd_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Volgograd')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_voronezh')
async def process_btn_voronezh_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Voronezh')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_kaluga')
async def process_btn_kaluga_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Kaluga')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_krasnodar')
async def process_btn_krasnodar_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Krasnodar')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_krasnoyarsk')
async def process_btn_krasnoyarsk_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Krasnoyarsk')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_nn')
async def process_btn_nn_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='NN')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_rostov')
async def process_btn_rostov_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Rostov')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_samara')
async def process_btn_samara_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Samara')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_saratov')
async def process_btn_saratov_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Saratov')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_ufa')
async def process_btn_ufa_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Ufa')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_yaroslavl')
async def process_btn_yaroslavl_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Yaroslavl')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_sochi')
async def process_btn_sochi_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Sochi')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_kazan')
async def process_btn_kazan_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(city='Kazan')
    await state.set_state(FSMFillVacancy.fill_payments)
    await callback.message.edit_text(text="Выберите частоту выплат", reply_markup=keyboard_payments)
    await callback.answer()


@router.callback_query(F.data == 'btn_two_month_payments')
async def process_btn_two_month_payments_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(count_payments='Два раза в месяц')
    await state.set_state(FSMFillVacancy.fill_detailed_info)
    await callback.message.edit_text(text="Введите дополнительную информацию о вакансии")
    await callback.answer()


@router.callback_query(F.data == 'btn_one_month_payments')
async def process_btn_one_month_payments_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(count_payments='Раз в месяц')
    await state.set_state(FSMFillVacancy.fill_detailed_info)
    await callback.message.edit_text(text="Введите дополнительную информацию о вакансии")
    await callback.answer()


@router.callback_query(F.data == 'btn_one_week_payments')
async def process_btn_one_week_payments_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(count_payments='Раз в неделю')
    await state.set_state(FSMFillVacancy.fill_detailed_info)
    await callback.message.edit_text(text="Введите дополнительную информацию о вакансии")
    await callback.answer()


@router.callback_query(F.data == 'btn_project_payments')
async def process_btn_project_payments_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(count_payments='За проект')
    await state.set_state(FSMFillVacancy.fill_detailed_info)
    await callback.message.edit_text(text="Введите дополнительную информацию о вакансии")
    await callback.answer()


@router.callback_query(F.data == 'btn_no_payments')
async def process_btn_no_payments_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(count_payments='Не указано')
    await state.set_state(FSMFillVacancy.fill_detailed_info)
    await callback.message.edit_text(text="Введите дополнительную информацию о вакансии (осторожн, если тг разобьет текст на 2 сообщения, вторая часть заполнит навыки")
    await callback.answer()


@router.message(StateFilter(FSMFillVacancy.fill_detailed_info))
async def process_detailed_information_sent(message: Message, state: FSMContext):
    await state.update_data(detailed_information=message.text)
    await state.set_state(FSMFillVacancy.fill_skills)
    await message.answer(text="Укажите требуемые навыки для вакансии через запятую (можно пропустить)", reply_markup=keyboard_skip)


@router.message(StateFilter(FSMFillVacancy.fill_skills))
async def process_skills_sent(message: Message, state: FSMContext):
    await state.update_data(skills=message.text)
    await state.set_state(FSMFillVacancy.fill_confirmation)
    await message.answer(text="Мы получили данные о вакансии, выберите дальнейшее действие", reply_markup=keyboard_choice_salary)


@router.callback_query(F.data == 'btn_skip')
async def process_btn_skip_click(callback: CallbackQuery, state: FSMContext):
    await state.update_data(skills="")
    await state.set_state(FSMFillVacancy.fill_confirmation)
    await callback.message.answer(text="Мы получили данные о вакансии, выберите дальнейшее действие", reply_markup=keyboard_choice_salary)
    await callback.answer()


@router.callback_query(F.data == 'btn_again_fill')
async def again_fill(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(FSMFillVacancy.fill_title)
    await callback.message.answer(text="Введите название вакансии")
    await callback.answer()


@router.callback_query(F.data == 'btn_send_prediction')
async def confirm_prediction(callback: CallbackQuery, state: FSMContext):
    await callback.message.edit_text(text="Начинаем рассчитывать...")
    await callback.answer()
    await tg_generate_vacancy_data_for_endpoint_request(callback, state)


