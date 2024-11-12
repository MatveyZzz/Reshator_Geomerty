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
    QHBoxLayout,
)
from PyQt6.QtGui import QDoubleValidator


class ShapeSelectionScreen(QWidget):
    """Экран выбора фигуры и типа расчета"""

    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        # Основной макет экрана
        layout = QVBoxLayout()

        # Заголовок экрана
        layout.addWidget(QLabel("Выберите геометрическую фигуру"))

        # Выбор фигуры
        self.shape_combo = QComboBox()
        self.shape_combo.addItems(["Окружность", "Квадрат"])
        layout.addWidget(self.shape_combo)

        # Выбор типа расчета
        layout.addWidget(QLabel("Выберите действие"))
        self.action_combo = QComboBox()
        self.action_combo.addItems(["Длина окружности", "Площадь"])
        layout.addWidget(self.action_combo)

        # Кнопка перехода к следующему экрану
        next_button = QPushButton("Далее")
        next_button.clicked.connect(self.go_to_input_screen)
        layout.addWidget(next_button)

        self.setLayout(layout)

    def go_to_input_screen(self):
        # Получаем текущий выбор фигуры и действия
        shape = self.shape_combo.currentText()
        action = self.action_combo.currentText()

        # Переходим к следующему экрану
        self.parent.show_input_screen(shape, action)


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
