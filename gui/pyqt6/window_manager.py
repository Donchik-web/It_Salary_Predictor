opened_windows = []

def open_login_with_pwd(window):
    """Открывает окно входа с использованием пароля"""
    from gui.pyqt6.login_windows.login_with_pwd import setup_login_with_pwd_window

    window.hide()
    login_pwd_window = setup_login_with_pwd_window()
    opened_windows.append(login_pwd_window)
    login_pwd_window.show()

    return login_pwd_window


def open_login_with_token(window):
    """Открывает окно входа с использованием токена"""
    from gui.pyqt6.login_windows.login_with_token import setup_login_with_token_window

    window.hide()
    login_token_window = setup_login_with_token_window()
    opened_windows.append(login_token_window)
    login_token_window.show()

    return login_token_window


def open_registration(window):
    """Открывает окно регистрации"""
    from gui.pyqt6.registration_window.registration import setup_registration_window

    window.hide()
    reg_window = setup_registration_window()
    opened_windows.append(reg_window)
    reg_window.show()

    return reg_window


def open_vacancy_data_window(window):
    """Открывает окно заполнения данных о вакансии"""
    from gui.pyqt6.vacancy_window.vacancy_data import setup_vacancy_info_window

    window.hide()
    vacancy_data_window = setup_vacancy_info_window()
    opened_windows.append(vacancy_data_window)
    vacancy_data_window.show()

    return vacancy_data_window


def open_approximate_salary_window(window, approximate_salary):
    """Открывает окно заполнения данных о вакансии"""
    from gui.pyqt6.vacancy_window.approximate_salary import setup_salary_window

    window.hide()
    salary_window = setup_salary_window(approximate_salary, window)
    opened_windows.append(salary_window)
    salary_window.show()

    return salary_window


def close_salary_open_vacancy(salary_window, vacancy_data_window):
    salary_window.close()

    if salary_window in opened_windows:
        opened_windows.remove(salary_window)

    vacancy_data_window.show()
    return vacancy_data_window