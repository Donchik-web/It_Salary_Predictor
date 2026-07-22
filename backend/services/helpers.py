import uuid
import random

from sqlalchemy.orm import Session
from fastapi import HTTPException

from database.tables.tables import Users
from settings.main_utils import hash_password, generate_jwt_token, verify_password
from backend.schemas.validators import UserRegistration, LoginRequest, EmailRegistrationRequest, VacancyRequest
from settings.main_utils import connect_smtp_server
from ml.predictor_service import predict_salary, vacancy_dict_to_dataframe

email_code_users = {}


def generate_send_confirm_code(email_req: EmailRegistrationRequest):
    """Генерация кода подтверждения"""
    generate_code = random.randint(100, 999)

    try:
        if connect_smtp_server(email_req.email, generate_code):
            email_code_users[email_req.email] = generate_code
            return {"message": f"Код подтверждения отправлен на {email_req.email}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Не удалось отправить письмо: {str(e)}")


def process_registration_fastAPI(user_data: UserRegistration, session: Session):
    """Создание пользователя в БД после усешной регистрации + токен"""
    if not user_data.email or "@" not in user_data.email:
        raise HTTPException(status_code=400, detail="Введите корректный e‑mail")
    if not user_data.code:
        raise HTTPException(status_code=400, detail="Введите код подтверждения")
    if not user_data.pwd:
        raise HTTPException(status_code=400, detail="Введите пароль")
    if not user_data.pwd_confirm or user_data.pwd_confirm != user_data.pwd:
        raise HTTPException(status_code=400, detail="Введите пароль подтверждения")

    if user_data.email not in email_code_users:
        raise HTTPException(status_code=400, detail="Сначала отправьте код на email")

    try:
        existing_user = session.query(Users).filter(Users.email == user_data.email).first()
        if existing_user:
            raise HTTPException(status_code=401, detail="Такой пользователь уже существует")

        if str(email_code_users.get(user_data.email)) == str(user_data.code):
            del email_code_users[user_data.email]

            user_id = uuid.uuid4()
            token = generate_jwt_token(str(user_id), user_data.email)

            user = Users(
                id=user_id,
                email=user_data.email,
                hash_pwd=hash_password(user_data.pwd),
                token=token
            )

            session.add(user)
            session.commit()

            return {
                "message": "Регистрация успешна",
                "access_token": token,
                "email": user_data.email
            }
        else:
            raise HTTPException(status_code=400, detail="Неверный код подтверждения")
    except HTTPException:
        raise
    except Exception as e:
        print(f"Ошибка: {e}")
        raise HTTPException(status_code=500, detail="Ошибка сервера")


def process_login_fastAPI(data: LoginRequest, session: Session):
    """Вход в аккаунт"""
    if not data.email or "@" not in data.email:
        raise HTTPException(status_code=400, detail="Введите корректный e‑mail")
    if not data.pwd:
        raise HTTPException(status_code=400, detail="Введите пароль")

    try:
        existing_user = session.query(Users).filter(Users.email == data.email).first()
        if not existing_user:
            raise HTTPException(status_code=401, detail="Такой пользователь не существует")

        if not verify_password(data.pwd, existing_user.hash_pwd):
            raise HTTPException(status_code=401, detail="Неверный пароль")

        return {"message": f"Добро пожаловать, {data.email}",
                "access_token": existing_user.token,
                "user_id": existing_user.id}

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {e}")


def process_vacancy_data(vacancy_data: VacancyRequest):
    """Передача информации о вакансии для предикта"""
    if not vacancy_data.title:
        raise HTTPException(status_code=400, detail="Введите название вакансии")
    if not vacancy_data.detailed_information:
        raise HTTPException(status_code=400, detail="Подробно опишите информацию, связанную с вакансией (о компании, цели, что ожидают, что придется делать ...")

    salary = predict_salary(vacancy_dict_to_dataframe(dict(vacancy_data)))

    return {
        "message": "Предсказание выполнено",
        "predicted_salary_text": f"Примерная зарплата по требованиям для вакансии - {salary} ₽",
        "predicted_salary": f"{salary} ₽"
    }