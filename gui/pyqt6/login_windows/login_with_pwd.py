from PyQt6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QWidget, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt
from gui.pyqt6.utils_forms import process_login_user_with_pwd


def setup_login_with_pwd_window():
    """Логин с паролем"""
    login_window = QMainWindow()
    login_window.setWindowTitle("It_Salary_Predictor")
    login_window.setGeometry(500, 350, 600, 300)

    central_widget = QWidget()
    login_window.setCentralWidget(central_widget)

    main_layout = QVBoxLayout(central_widget)

    QLtitle = QLabel("Вход с помощью пароля")
    QLtitle.setStyleSheet("font-size: 40px; font-weight: bold;")
    QLtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_layout.addWidget(QLtitle)

    QLemail = QLabel("Email")
    QLemail.setStyleSheet("font-size: 20px; font-weight: bold;")
    QLemail.setAlignment(Qt.AlignmentFlag.AlignVCenter)
    main_layout.addWidget(QLemail)

    email_edit = QLineEdit()
    email_edit.setPlaceholderText("Введите email")
    main_layout.addWidget(email_edit)

    QLpassword = QLabel("Пароль")
    QLpassword.setStyleSheet("font-size: 20px; font-weight: bold;")
    main_layout.addWidget(QLpassword)

    pwd_edit = QLineEdit()
    pwd_edit.setEchoMode(QLineEdit.EchoMode.Password)
    pwd_edit.setPlaceholderText("Введите пароль")
    main_layout.addWidget(pwd_edit)

    login_with_pwd_btn = QPushButton("Войти")
    login_with_pwd_btn.clicked.connect(lambda: process_login_user_with_pwd(login_window, email_edit, pwd_edit))
    main_layout.addWidget(login_with_pwd_btn)

    from gui.pyqt6.window_manager import open_registration, open_login_with_token
    reg_log_btn = QHBoxLayout()
    reg_btn = QPushButton("Регистрация")
    reg_btn.clicked.connect(lambda: open_registration(login_window))
    reg_log_btn.addWidget(reg_btn)

    login_with_token_btn = QPushButton("Войти (через токен)")
    login_with_token_btn.clicked.connect(lambda: open_login_with_token(login_window))
    reg_log_btn.addWidget(login_with_token_btn)

    main_layout.addLayout(reg_log_btn)

    return login_window