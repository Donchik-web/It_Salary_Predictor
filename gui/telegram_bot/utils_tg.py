import re
import json
import requests

from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from settings.main_utils import API_URL


async def tg_generate_vacancy_data_for_endpoint_request(callback: CallbackQuery, state: FSMContext):
    """Собирает данные из state и отправляет в FastAPI"""
    data = await state.get_data()

    skills_text = data['skills'].strip()
    if skills_text:
        skills_text = re.sub(r'[,\s\n\t]+', ',', skills_text)

        skills = [s.strip() for s in skills_text.split(",") if s.strip()]
    else:
        skills = ["Не указано"]

    vacancy_data = {
        "title": data['title'],
        "experience": data['experience'],
        "work_format": data['work_format'],
        "common_employment": data['common_employment'],
        "work_schedule": data['work_schedule'],
        "work_hours": data['work_hours'],
        "name_company": "",
        "city": data['city'],
        "address": "",
        "count_payments": data['count_payments'],
        "detailed_information": data['detailed_information'],
        "skills": skills,
    }

    print(json.dumps(vacancy_data, indent=4, ensure_ascii=False))

    await push_vacancy_data_endpoint(callback, state, vacancy_data)


async def push_vacancy_data_endpoint(callback: CallbackQuery, state: FSMContext, vacancy_data: dict):
    """Отправляет информацию о вакансии на эндпоинт"""
    try:
        response = requests.post(f"{API_URL}/auth/vacancy-data", json=vacancy_data)

        if response.status_code == 200:
            await callback.message.edit_text(text=f"Примерная зарплата по данным - {response.json()['predicted_salary']}")
            await state.clear()
            await callback.answer()
        else:
            error = response.json().get("detail", "Ошибка отправки запроса с информацией о вакансии")
            await callback.message.edit_text(text=f"Возникла ошибка: {error}")
            await callback.answer()

    except requests.exceptions.ConnectionError:
        await callback.message.edit_text(text="Сервер не доступен")
        await callback.answer()

    except Exception as e:
        await callback.message.edit_text(text=f"Ошибка {str(e)})")
        await callback.answer()