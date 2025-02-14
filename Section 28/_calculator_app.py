from PyQt6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
    QCheckBox,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
)
import sys
from PyQt6.QtGui import QPixmap, QFont
import math
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")
        # 12                +                   14
        # previous input    current operator    current input
        self.current_input = "0"
        self.previous_input = ""
        self.current_operator = ""

        layout = QGridLayout()
        self.setLayout(layout)

        self.display = QLabel("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(self.display, 0, 0, 1, 4)

        buttons = [QPushButton(str(i)) for i in range(10)]
        operators = ["+", "-", "*", "/"]
        operator_buttons = [QPushButton(op) for op in operators]
        for button in operator_buttons:
            button.clicked.connect(operator_button_clicked)

        equal_button = QPushButton("=")
        clear_button = QPushButton("C")

        for i, button in enumerate(buttons):
            row, col = divmod(i, 3)
            layout.addWidget(button, row + 1, col)

        # adding event handling method to buttons
        for button in buttons:
            button.clicked.connect(self.number_button_clicked)

        for i, op_button in enumerate(operator_buttons):
            layout.addWidget(op_button, i + 1, 3)
        layout.addWidget(equal_button, 4, 1)
        layout.addWidget(clear_button, 4, 2)

    # metoda za hendlanje buttona sa brojevima
    def number_button_clicked(self):
        digit = self.sender().text()
        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        self.display.setText(self.current_input)

    def operator_button_clicked(self):
        operator = self.sender().text()
        if self.current_operator == "":
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input == "0"
        else:
            # calculate result
            self.current_operator = operator
            self.previous_input = self.current_input
            self.current_input == "0"


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
