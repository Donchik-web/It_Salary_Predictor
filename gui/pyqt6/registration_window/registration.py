from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from gui.pyqt6.utils_forms import push_code_confirm, process_registration
from gui.pyqt6.window_manager import open_login_with_pwd, open_login_with_token


def setup_registration_window():
    window = QMainWindow()
    window.setWindowTitle("It_Salary_Predictor")
    window.setGeometry(500, 350, 600, 300)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    main_layout = QVBoxLayout(central_widget)

    QLtitle = QLabel("Регистрация")
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

    QLcode = QLabel("Код подтверждения")
    QLcode.setStyleSheet("font-size: 20px; font-weight: bold;")
    main_layout.addWidget(QLcode)

    code_layout = QHBoxLayout()
    code_edit = QLineEdit()
    code_edit.setPlaceholderText("Введите код")
    code_push_btn = QPushButton("Отправить код")
    code_push_btn.clicked.connect(lambda: push_code_confirm(email_edit, code_push_btn))

    code_layout.addWidget(code_edit)
    code_layout.addWidget(code_push_btn)
    main_layout.addLayout(code_layout)

    QLpassword = QLabel("Пароль")
    QLpassword.setStyleSheet("font-size: 20px; font-weight: bold;")
    main_layout.addWidget(QLpassword)

    pwd_edit = QLineEdit()
    pwd_edit.setEchoMode(QLineEdit.EchoMode.Password)
    pwd_edit.setPlaceholderText("Введите пароль")
    main_layout.addWidget(pwd_edit)

    QLconfirm_password = QLabel("Подтвердите пароль")
    QLconfirm_password.setStyleSheet("font-size: 20px; font-weight: bold;")
    main_layout.addWidget(QLconfirm_password)

    pwd_confirm_edit = QLineEdit()
    pwd_confirm_edit.setEchoMode(QLineEdit.EchoMode.Password)
    pwd_confirm_edit.setPlaceholderText("Повторите пароль")
    main_layout.addWidget(pwd_confirm_edit)

    main_layout.addStretch()

    register_btn = QPushButton("Зарегистрироваться")
    register_btn.clicked.connect(lambda: process_registration(window, email_edit, code_edit, pwd_edit, pwd_confirm_edit))
    main_layout.addWidget(register_btn)

    logins_btn = QHBoxLayout()
    login_with_pwd_btn = QPushButton("Войти (с помощью пароля)")
    login_with_pwd_btn.clicked.connect(lambda: open_login_with_pwd(window))
    logins_btn.addWidget(login_with_pwd_btn)

    login_with_token_btn = QPushButton("Войти (через токен)")
    login_with_token_btn.clicked.connect(lambda: open_login_with_token(window))
    logins_btn.addWidget(login_with_token_btn)

    main_layout.addLayout(logins_btn)

    return window
