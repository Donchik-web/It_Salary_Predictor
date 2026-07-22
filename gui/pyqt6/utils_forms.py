import re
import requests

from dotenv import load_dotenv
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QMessageBox, QMainWindow, QLabel
from gui.pyqt6.window_manager import open_vacancy_data_window, open_approximate_salary_window
from settings.main_utils import API_URL

load_dotenv()


def add_field(main_layout, label_text, widget):
    """Строит элементы Qt"""
    label = QLabel(label_text)
    label.setStyleSheet("font-size: 16px; font-weight: bold;")
    main_layout.addWidget(label)
    main_layout.addWidget(widget)
    return widget


def push_code_confirm(email_le: QLineEdit, btn: QPushButton):
    """Отправляет email на бэкенд для получения кода"""
    email = email_le.text().strip()
    if not email or "@" not in email:
        QMessageBox.warning(email_le.window(), "Ошибка", "Введите корректный e‑mail")
        return

    window = email_le.window()
    window.setEnabled(False)
    btn.setText("Отправка...")
    QApplication.processEvents()

    try:
        response = requests.post(f"{API_URL}/auth/send-email-code", json={"email": email})

        if response.status_code == 200:
            QMessageBox.information(window, "Код отправлен", f"Код подтверждения отправлен на {email}")
        else:
            error = response.json().get("detail", "Ошибка отправки")
            QMessageBox.warning(window, "Ошибка", error)

    except requests.exceptions.ConnectionError:
        QMessageBox.warning(window, "Ошибка", "Сервер не доступен")
    except Exception as e:
        QMessageBox.warning(window, "Ошибка", f"Неизвестная ошибка: {str(e)}")
    finally:
        window.setEnabled(True)
        btn.setText("Отправить снова")



def process_registration(window: QMainWindow, email_le: QLineEdit, code_le: QLineEdit,
                         pwd_le: QLineEdit, pwd_confirm_le: QLineEdit):
    """Регистрация пользователя"""
    email = email_le.text().strip()
    code = code_le.text().strip()
    pwd = pwd_le.text().strip()
    pwd_confirm = pwd_confirm_le.text().strip()

    try:
        response = requests.post(f"{API_URL}/auth/registration",
            json={
                "email": email,
                "code": code,
                "pwd": pwd,
                "pwd_confirm": pwd_confirm}
        )

        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            print(token)

            QMessageBox.information(window, "Успех", f"Регистрация успешна!")
            open_vacancy_data_window(window)

        else:
            error = response.json().get("detail", "Ошибка регистрации")
            QMessageBox.warning(window, "Ошибка", error)

    except requests.exceptions.ConnectionError:
        QMessageBox.warning(window, "Ошибка", "Сервер не доступен")

    except Exception as e:
        QMessageBox.warning(window, "Ошибка", str(e))


def process_login_user_with_pwd(window: QMainWindow, email_le: QLineEdit, pwd_le: QLineEdit):
    """Вход в учетку через пароль"""
    email = email_le.text().strip()
    pwd = pwd_le.text().strip()

    try:
        response = requests.post(f"{API_URL}/auth/login-pwd", json={"email": email, "pwd": pwd})

        if response.status_code == 200:
            data = response.json()
            token = data["access_token"]
            print(token)

            QMessageBox.information(window, "Успех", "Вход выполнен!")
            open_vacancy_data_window(window)

        else:
            error = response.json().get("detail", "Ошибка регистрации")
            QMessageBox.warning(window, "Ошибка", error)

    except requests.exceptions.ConnectionError:
        QMessageBox.warning(window, "Ошибка", "Сервер не доступен")

    except Exception as e:
        QMessageBox.warning(window, "Ошибка", str(e))


def process_login_user_with_token(window: QMainWindow, token_le: QLineEdit):
    """Вход в учетку через пароль"""
    token = token_le.text().strip()

    try:
        response = requests.post(f"{API_URL}/auth/login-token", headers = {"Authorization": f"Bearer {token}"})

        if response.status_code == 200:
            QMessageBox.information(window, "Успех", "Вход выполнен!")
            open_vacancy_data_window(window)

        else:
            error = response.json().get("detail", "Ошибка регистрации")
            QMessageBox.warning(window, "Ошибка", error)

    except requests.exceptions.ConnectionError:
        QMessageBox.warning(window, "Ошибка", "Сервер не доступен")

    except Exception as e:
        QMessageBox.warning(window, "Ошибка", str(e))


def generate_vacancy_data_for_endpoint_request(
        window: QMainWindow, title_edit, exp_combo, format_combo, employ_combo, schedule_combo,
        hours_combo, company_edit, city_combo, address_edit, payments_combo, detailed_text, skills_edit
):
    skills_text = skills_edit.text().strip()
    if skills_text:
        skills_text = re.sub(r'[,\s\n\t]+', ',', skills_text)

        skills = [s.strip() for s in skills_text.split(",") if s.strip()]
    else:
        skills = ["Не указано"]

    """Формирует словарь для отправки информации о вакансии"""
    vacancy_data = {
        "title": title_edit.text().strip(),
        "experience": exp_combo.currentText(),
        "work_format": format_combo.currentText(),
        "common_employment": employ_combo.currentText(),
        "work_schedule": schedule_combo.currentText(),
        "work_hours": hours_combo.currentText(),
        "name_company": company_edit.text().strip(),
        "city": city_combo.currentText(),
        "address": address_edit.text().strip(),
        "count_payments": payments_combo.currentText(),
        "detailed_information": detailed_text.toPlainText().strip(),
        "skills": skills,
    }

    push_vacancy_data_endpoint(window, vacancy_data)


def push_vacancy_data_endpoint(window: QMainWindow, vacancy_data: dict):
    """Отправляет информацию о вакансии на эндпоинт"""
    try:
        response = requests.post(f"{API_URL}/auth/vacancy-data", json=vacancy_data)

        if response.status_code == 200:
            open_approximate_salary_window(window, response.json()['predicted_salary'])
        else:
            error = response.json().get("detail", "Ошибка регистрации")
            QMessageBox.warning(window, "Ошибка", error)

    except requests.exceptions.ConnectionError:
        QMessageBox.warning(window, "Ошибка", "Сервер не доступен")

    except Exception as e:
        QMessageBox.warning(window, "Ошибка", str(e))
