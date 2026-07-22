from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from gui.pyqt6.window_manager import close_salary_open_vacancy


def setup_salary_window(approximate_salary: float, vacancy_window):
    window = QMainWindow()
    window.setWindowTitle("It_Salary_Predictor")
    window.setGeometry(650, 400, 100, 150)

    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    main_layout = QVBoxLayout(central_widget)

    QLtext = QLabel(f"Примерная зарплата - {approximate_salary}")
    QLtext.setStyleSheet("font-size: 30px;")
    QLtext.setAlignment(Qt.AlignmentFlag.AlignCenter)
    main_layout.addWidget(QLtext)

    main_layout.addStretch()

    close_btn = QPushButton("Закрыть")
    close_btn.clicked.connect(lambda: close_salary_open_vacancy(salary_window=window, vacancy_data_window=vacancy_window))
    main_layout.addWidget(close_btn)

    return window