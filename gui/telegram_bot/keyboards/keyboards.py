from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

btn_no_exp = InlineKeyboardButton(text="Нет опыта", callback_data="btn_no_exp")
btn_junior_exp = InlineKeyboardButton(text="1-3 года", callback_data="btn_junior_exp")
btn_middle_exp = InlineKeyboardButton(text="3-6 лет", callback_data="btn_middle_exp")
btn_senior_exp = InlineKeyboardButton(text="6+ лет", callback_data="btn_senior_exp")

btn_office_format = InlineKeyboardButton(text="Офис", callback_data="btn_office_format")
btn_remote_format = InlineKeyboardButton(text="Удалённо", callback_data="btn_remote_format")
btn_hybrid_format = InlineKeyboardButton(text="Гибрид", callback_data="btn_hybrid_format")
btn_no_format = InlineKeyboardButton(text="Не указано", callback_data="btn_no_format")

btn_full_employment = InlineKeyboardButton(text="Полная занятость", callback_data="btn_full_employment")
btn_part_employment = InlineKeyboardButton(text="Частичная занятость", callback_data="btn_part_employment")
btn_intern_employment = InlineKeyboardButton(text="Стажировка/Проект", callback_data="btn_intern_employment")

btn_classic_schedule = InlineKeyboardButton(text="Классический (5/2)", callback_data="btn_classic_schedule")
btn_free_schedule = InlineKeyboardButton(text="Свободный", callback_data="btn_free_schedule")
btn_other_schedule = InlineKeyboardButton(text="Другие", callback_data="btn_other_schedule")
btn_no_schedule = InlineKeyboardButton(text="Не указано", callback_data="btn_no_schedule")

btn_eight_hours = InlineKeyboardButton(text="8 часов", callback_data="btn_eight_hours")
btn_twelve_hours = InlineKeyboardButton(text="12 часов", callback_data="btn_twelve_hours")
btn_six_hours = InlineKeyboardButton(text="6 часов", callback_data="btn_six_hours")
btn_agree_hours = InlineKeyboardButton(text="По договоренности", callback_data="btn_agree_hours")
btn_other_hours = InlineKeyboardButton(text="Другие", callback_data="btn_other_hours")
btn_no_hours = InlineKeyboardButton(text="Не указано", callback_data="btn_no_hours")

btn_moscow = InlineKeyboardButton(text="Москва", callback_data="btn_moscow")
btn_spb = InlineKeyboardButton(text="Санкт-Петербург", callback_data="btn_spb")
btn_ekb = InlineKeyboardButton(text="Екатеринбург", callback_data="btn_ekb")
btn_novosibirsk = InlineKeyboardButton(text="Новосибирск", callback_data="btn_novosibirsk")
btn_vladivostok = InlineKeyboardButton(text="Владивосток", callback_data="btn_vladivostok")
btn_volgograd = InlineKeyboardButton(text="Волгоград", callback_data="btn_volgograd")
btn_voronezh = InlineKeyboardButton(text="Воронеж", callback_data="btn_voronezh")
btn_kaluga = InlineKeyboardButton(text="Калуга", callback_data="btn_kaluga")
btn_krasnodar = InlineKeyboardButton(text="Краснодар", callback_data="btn_krasnodar")
btn_krasnoyarsk = InlineKeyboardButton(text="Красноярск", callback_data="btn_krasnoyarsk")
btn_nn = InlineKeyboardButton(text="Нижний Новгород", callback_data="btn_nn")
btn_rostov = InlineKeyboardButton(text="Ростов-на-Дону", callback_data="btn_rostov")
btn_samara = InlineKeyboardButton(text="Самара", callback_data="btn_samara")
btn_saratov = InlineKeyboardButton(text="Саратов", callback_data="btn_saratov")
btn_ufa = InlineKeyboardButton(text="Уфа", callback_data="btn_ufa")
btn_yaroslavl = InlineKeyboardButton(text="Ярославль", callback_data="btn_yaroslavl")
btn_sochi = InlineKeyboardButton(text="Сочи", callback_data="btn_sochi")
btn_kazan = InlineKeyboardButton(text="Казань", callback_data="btn_kazan")

btn_two_month_payments = InlineKeyboardButton(text="Два раза в месяц", callback_data="btn_two_month_payments")
btn_one_month_payments = InlineKeyboardButton(text="Раз в месяц", callback_data="btn_one_month_payments")
btn_one_week_payments = InlineKeyboardButton(text="Раз в неделю", callback_data="btn_one_week_payments")
btn_project_payments = InlineKeyboardButton(text="За проект", callback_data="btn_project_payments")
btn_no_payments = InlineKeyboardButton(text="Не указано", callback_data="btn_no_payments")

btn_again_fill = InlineKeyboardButton(text="Заполнить заново", callback_data="btn_again_fill")
btn_send_prediction = InlineKeyboardButton(text="Предсказать", callback_data="btn_send_prediction")

keyboard_exp = InlineKeyboardMarkup(inline_keyboard=[[btn_no_exp], [btn_junior_exp], [btn_middle_exp], [btn_senior_exp]])
keyboard_format = InlineKeyboardMarkup(inline_keyboard=[[btn_office_format], [btn_remote_format], [btn_hybrid_format], [btn_no_format]])
keyboard_employment = InlineKeyboardMarkup(inline_keyboard=[[btn_full_employment], [btn_part_employment], [btn_intern_employment]])
keyboard_schedule = InlineKeyboardMarkup(inline_keyboard=[[btn_classic_schedule], [btn_free_schedule], [btn_other_schedule], [btn_no_schedule]])
keyboard_hours = InlineKeyboardMarkup(inline_keyboard=[[btn_eight_hours], [btn_twelve_hours], [btn_six_hours], [btn_agree_hours], [btn_other_hours], [btn_no_hours]])
keyboard_cities = InlineKeyboardMarkup(inline_keyboard=[
    [btn_moscow, btn_spb],
    [btn_ekb, btn_novosibirsk],
    [btn_vladivostok, btn_volgograd],
    [btn_voronezh, btn_kaluga],
    [btn_krasnodar, btn_krasnoyarsk],
    [btn_nn, btn_rostov],
    [btn_samara, btn_saratov],
    [btn_ufa, btn_yaroslavl],
    [btn_sochi, btn_kazan]
])
keyboard_payments = InlineKeyboardMarkup(inline_keyboard=[[btn_two_month_payments], [btn_one_month_payments], [btn_one_week_payments], [btn_project_payments], [btn_no_payments]])
keyboard_skip = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Пропустить', callback_data='btn_skip')]])
keyboard_choice_salary = InlineKeyboardMarkup(inline_keyboard=[[btn_again_fill, btn_send_prediction]])