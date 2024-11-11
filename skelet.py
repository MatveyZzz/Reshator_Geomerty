import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QStackedWidget,
    QMessageBox,
)
from PyQt6.QtGui import QDoubleValidator


class SelectScreen(QWidget):
    def __init__(self, main):
        super().__init__()

    def go_to_input(self):
        pass


class InputScreen(QWidget):
    def __init__(self, main):
        super().__init__()

    def set_params(self, shape, action):
        pass

    def calculate(self):
        pass

    def go_back(self):
        pass


class ResultScreen(QWidget):
    def __init__(self, main):
        super().__init__()

    def set_result(self, result):
        pass


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()

    def show_select(self):
        pass

    def show_input(self, shape, action):
        pass

    def show_result(self, result):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
