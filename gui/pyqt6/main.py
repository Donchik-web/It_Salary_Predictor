import sys

from PyQt6.QtWidgets import QApplication
from gui.pyqt6.registration_window.registration import setup_registration_window

app_QT = QApplication(sys.argv)

def main():
    window = setup_registration_window()
    window.show()
    sys.exit(app_QT.exec())


if __name__ == "__main__":
    main()