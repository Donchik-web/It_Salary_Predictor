from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from gui.pyqt6.utils_forms import process_login_user_with_token


def setup_login_with_token_window():
    """Логин с токеном"""
    login_window = QMainWindow()
    login_window.setWindowTitle("It_Salary_Predictor")
    login_window.setGeometry(500, 350, 600, 300)

    central_widget = QWidget()
    login_window.setCentralWidget(central_widget)

    main_layout = QVBoxLayout(central_widget)

    QLtitle = QLabel("Вход с помощью токена")
    QLtitle.setStyleSheet("font-size: 40px; font-weight: bold;")
    QLtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_layout.addWidget(QLtitle)

    QLtoken = QLabel("Токен")
    QLtoken.setStyleSheet("font-size: 20px; font-weight: bold;")
    QLtoken.setAlignment(Qt.AlignmentFlag.AlignVCenter)
    main_layout.addWidget(QLtoken)

    token_edit = QLineEdit()
    token_edit.setPlaceholderText("Введите токен")
    main_layout.addWidget(token_edit)

    login_with_pwd_btn = QPushButton("Войти")
    login_with_pwd_btn.clicked.connect(lambda: process_login_user_with_token(login_window, token_edit))
    main_layout.addWidget(login_with_pwd_btn)

    from gui.pyqt6.window_manager import open_registration, open_login_with_pwd
    reg_log_btn = QHBoxLayout()
    reg_btn = QPushButton("Регистрация")
    reg_btn.clicked.connect(lambda: open_registration(login_window))
    reg_log_btn.addWidget(reg_btn)

    login_with_pwd_btn = QPushButton("Войти (с помощью пароля)")
    login_with_pwd_btn.clicked.connect(lambda: open_login_with_pwd(login_window))
    reg_log_btn.addWidget(login_with_pwd_btn)

    main_layout.addLayout(reg_log_btn)

    return login_window