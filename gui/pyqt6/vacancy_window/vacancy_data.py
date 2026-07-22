from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit,
                             QPushButton, QComboBox, QScrollArea, QTextEdit)
from PyQt6.QtCore import Qt
from settings.main_utils import cities_decode
from gui.pyqt6.utils_forms import add_field, generate_vacancy_data_for_endpoint_request


def setup_vacancy_info_window():
    """Главное окно для ввода инофрмации о ваакансии, для которой необходимо будет предсказать зарплату"""
    window = QMainWindow()
    window.setWindowTitle("It_Salary_Predictor")
    window.setGeometry(500, 50, 1000, 900)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    scroll = QScrollArea()
    scroll.setWidgetResizable(True)
    scroll.setWidget(central_widget)
    window.setCentralWidget(scroll)

    main_layout = QVBoxLayout(central_widget)

    QLtitle = QLabel("Информация о вакансии")
    QLtitle.setStyleSheet("font-size: 40px; font-weight: bold;")
    QLtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_layout.addWidget(QLtitle)

    title_vacancy_edit = add_field(main_layout, "Название вакансии:", QLineEdit())
    title_vacancy_edit.setPlaceholderText("например: Python разработчик")

    experience_combo = QComboBox()
    experience_combo.addItems(["Нет опыта", "1-3 года", "3-6 лет", "6+ лет"])
    add_field(main_layout, "Опыт работы:", experience_combo)

    work_format_combo = QComboBox()
    work_format_combo.addItems(["Офис", "Удалённо", "Гибрид", "Не указано"])
    add_field(main_layout, "Формат работы:", work_format_combo)

    employment_combo = QComboBox()
    employment_combo.addItems(["Полная занятость", "Частичная занятость", "Стажировка/Проект"])
    add_field(main_layout, "Занятость:", employment_combo)

    schedule_combo = QComboBox()
    schedule_combo.addItems(["Классический (5/2)", "Свободный", "Другие", "Не указано"])
    add_field(main_layout, "График работы:", schedule_combo)

    hours_combo = QComboBox()
    hours_combo.addItems(["8 часов", "12 часов", "6 часов", "По договоренности", "Другие", "Не указано"])
    add_field(main_layout, "Рабочие часы:", hours_combo)

    company_edit = add_field(main_layout, "Компания (необязательно):", QLineEdit())
    company_edit.setPlaceholderText("например: ООО Ромашка")

    city_names = [city_name for code, city_name in cities_decode.items()]
    city_combo = QComboBox()
    city_combo.addItems(city_names)
    add_field(main_layout, "Город:", city_combo)

    address_edit = add_field(main_layout, "Адрес (необязательно):", QLineEdit())
    address_edit.setPlaceholderText("улица, дом")

    payments_combo = QComboBox()
    payments_combo.addItems(["Два раза в месяц", "Раз в месяц", "Раз в неделю", "За проект", "Не указано"])
    add_field(main_layout, "Выплаты:", payments_combo)

    detailed_edit = QTextEdit()
    detailed_edit.setPlaceholderText("Подробное описание вакансии, требования, условия...")
    detailed_edit.setMaximumHeight(150)
    add_field(main_layout, "Подробное описание:", detailed_edit)

    skills_edit = add_field(main_layout, "Навыки (через запятую):", QLineEdit())
    skills_edit.setPlaceholderText("например: Python, SQL, Django, Git")

    main_layout.addStretch()

    submit_btn = QPushButton("Предсказать зарплату")
    submit_btn.clicked.connect(
            lambda: generate_vacancy_data_for_endpoint_request(window, title_vacancy_edit, experience_combo,
                                                 work_format_combo, employment_combo, schedule_combo, hours_combo, company_edit,
                                                 city_combo, address_edit, payments_combo, detailed_edit, skills_edit
        )
    )

    main_layout.addWidget(submit_btn)

    return window
