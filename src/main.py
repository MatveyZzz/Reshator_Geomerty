import sys
import math
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
    QFileDialog,
)


from PyQt6.QtGui import QDoubleValidator, QPainter, QPen, QColor
from PyQt6.QtCore import Qt


class BaseScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

    def show_message(self, title, text):
        QMessageBox.warning(self, title, text)


class ShapeSelectionScreen(BaseScreen):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Выберите фигуру"))
        self.comboFigura = QComboBox()
        self.comboFigura.addItems(["Окружность", "Квадрат"])
        layout.addWidget(self.comboFigura)
        layout.addWidget(QLabel("Выберите действие"))
        self.comboDeistvie = QComboBox()
        self.comboDeistvie.addItems(["Длина", "Площадь", "Периметр"])
        layout.addWidget(self.comboDeistvie)
        nextButton = QPushButton("Далее")
        nextButton.clicked.connect(self.go_to_input_screen)
        layout.addWidget(nextButton)
        self.setLayout(layout)

    def go_to_input_screen(self):
        figura = self.comboFigura.currentText()
        deistvie = self.comboDeistvie.currentText()
        self.parent.show_input_screen(figura, deistvie)


class InputScreen(BaseScreen):
    def __init__(self, parent):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.param_input = QLineEdit()
        self.param_input.setValidator(QDoubleValidator(0.0, 100000.0, 2))
        self.layout.addWidget(QLabel("Введите параметр:"))
        self.layout.addWidget(self.param_input)
        calc_button = QPushButton("Рассчитать")
        calc_button.clicked.connect(self.calculate_result)
        self.layout.addWidget(calc_button)
        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.go_back)
        self.layout.addWidget(back_button)
        self.setLayout(self.layout)
        self.param_label = QLabel("Введите радиус:")

    def set_parameters(self, figura, deistvie):
        self.figura = figura
        self.deistvie = deistvie
        self.param_input.clear()
        if figura == "Окружность":
            self.param_label
        elif figura == "Квадрат":
            self.param_label.setText("Введите сторону:")
        elif figura == "Треугольник":
            self.param_label.setText("Введите длину стороны:")
        self.layout.insertWidget(0, self.param_label)

    def calculate_result(self):
        try:
            value = float(self.param_input.text())
            if self.figura == "Окружность" and self.deistvie == "Длина":
                result = 2 * math.pi * value
            elif self.figura == "Окружность" and self.deistvie == "Площадь":
                result = math.pi * (value**2)
            elif self.figura == "Квадрат" and self.deistvie == "Площадь":
                result = value**2
            else:
                result = "Ошибка"
            self.parent.show_result_screen(result, self.figura, value)
        except ValueError:
            self.show_message("Ошибка", "Введите корректное число.")

    def go_back(self):
        self.parent.show_selection_screen()


class ResultScreen(BaseScreen):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QVBoxLayout()
        self.result_label = QLabel("Результат:")
        layout.addWidget(self.result_label)
        self.save_button = QPushButton("Сохранить результат")
        self.save_button.clicked.connect(self.save_result)
        layout.addWidget(self.save_button)
        new_calc_button = QPushButton("Новый расчет")
        new_calc_button.clicked.connect(self.parent.show_selection_screen)
        layout.addWidget(new_calc_button)
        self.setLayout(layout)

    def set_result(self, result, figura, param):
        if result == str():
            self.result_label.setText(f"Результат: {round(result, 2)}")
        else:
            self.result_label.setText(f"Результат: {round(result, 2)}")
        self.figura = figura
        self.param = param
        self.update()

    def save_result(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Сохранить результат", "", "Text Files (*.txt)"
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(f"Фигура: {self.figura}\n")
                file.write(f"Параметр: {self.param}\n")
                file.write(f"Результат: {self.result_label.text()}\n")
            self.show_message("Сохранение", "Результат сохранен")

    def paintEvent(self, event):
        if not hasattr(self, "figura") or not hasattr(self, "param"):
            return
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        pen = QPen(QColor(0, 100, 250), 3, Qt.PenStyle.SolidLine)
        painter.setPen(pen)
        if self.figura == "Окружность":
            radius = int(self.param)
            painter.drawEllipse(130, 10, radius, radius)
        elif self.figura == "Квадрат":
            side = int(self.param)
            painter.drawRect(110, 15, side, side)


class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Решатор")
        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.selection_screen = ShapeSelectionScreen(self)
        self.input_screen = InputScreen(self)
        self.result_screen = ResultScreen(self)
        self.k = ResultScreen(self)
        self.central_widget.addWidget(self.selection_screen)
        self.central_widget.addWidget(self.input_screen)
        self.central_widget.addWidget(self.result_screen)

    def show_selection_screen(self):
        self.central_widget.setCurrentWidget(self.selection_screen)

    def show_input_screen(self, figura, deistvie):
        self.input_screen.set_parameters(figura, deistvie)
        self.central_widget.setCurrentWidget(self.input_screen)

    def show_result_screen(self, result, figura, param):
        self.result_screen.set_result(result, figura, param)
        self.central_widget.setCurrentWidget(self.result_screen)
        self.k.paintEvent(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
