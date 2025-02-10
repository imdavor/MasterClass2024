from PyQt6.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
    QCheckBox,
)
import sys
from PyQt6.QtGui import QPixmap, QFont
import math


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0, 0, 400, 300)

        number_label = QLabel("Enter a number:", self)
        number_label.move(20, 20)

        self.number_input = QLineEdit(self)
        self.number_input.move(200, 20)

        calculate_button = QPushButton("Find root", self)
        calculate_button.move(200, 60)

        self.result_label = QLabel("Result:", self)
        self.result_label.move(200, 100)

        calculate_button.clicked.connect(self.calculate_self_root)

    def calculate_self_root(self):
        number = float(self.number_input.text())
        square_root = math.sqrt(number)
        if square_root.is_integer():
            self.result_label.setText(f"Square root is {square_root}")
        else:
            msg = QMessageBox.warning(
                self, "Warning!", "The number is not a perfect square!"
            )


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
