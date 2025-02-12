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

        layout = QGridLayout()
        self.setLayout(layout)

        display = QLabel("0")
        display.setAlignment(Qt.AlignmentFlag.AlignRight)

        layout.addWidget(display, 0, 0, 1, 4)

        buttons = [QPushButton(str(i)) for i in range(10)]

        for i, button in enumerate(buttons):
            row, col = divmod(i, 3)
            layout.addWidget(button, row + 1, col)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
