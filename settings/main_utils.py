import bcrypt
import os
import smtplib
import jwt

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
API_URL = "http://localhost:8000"

cities_decode = {
    1: 'Moscow',
    2: 'SPB',
    3: 'Ekaterinburg',
    4: 'Novosibirsk',
    22: 'Vladivostok',
    24: 'Volgograd',
    26: 'Voronezh',
    43: 'Kaluga',
    53: 'Krasnodar',
    54: 'Krasnoyarsk',
    66: 'NN',
    76: 'Rostov',
    78: 'Samara',
    79: 'Saratov',
    99: 'Ufa',
    112: 'Yaroslavl',
    237: 'Sochi',
    888: 'Kazan',
}


def connect_smtp_server(email: str, generate_code: int):
    """Подключение к серверу для отправки кода подтвержедния"""
    server = os.getenv("SMTP_SERVER")
    sender_email = os.getenv('SMTP_EMAIL')
    password = os.getenv('SMTP_PASSWORD')

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = email
    msg["Subject"] = "Код подтверждения"

    email_text = f"Ваш код подтверждения для регистрации {generate_code}!"

    msg.attach(MIMEText(email_text, 'plain', 'utf-8'))  # Отправка сообщения на email

    # Отправка через SMTP
    with smtplib.SMTP_SSL(server, 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)
        return True


def hash_password(password: str) -> str:
    """Хеширование пароля"""
    salt = bcrypt.gensalt(rounds=12, prefix=b"2b")
    return bcrypt.hashpw(password.encode("utf-8"), salt).decode("utf-8")


def verify_password(password: str, hash_pwd: str) -> bool:
    """Проверка введенного пароля"""
    return bcrypt.checkpw(password.encode("utf-8"), hash_pwd.encode("utf-8"))


def generate_jwt_token(user_id: str, email: str) -> str:
    """JWT токен"""
    token = jwt.encode(
        {
            "sub": str(user_id),
            "email": email,
        }, SECRET_KEY, algorithm=ALGORITHM
    )

    return token


def verify_token(token: str):
    """Проверка токена"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.PyJWTError:
        return None
