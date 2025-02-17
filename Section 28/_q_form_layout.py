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
    QLineEdit,
    QFormLayout,
)
import sys
from PyQt6.QtGui import QPixmap, QFont
import math


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Form layout")
        self.setGeometry(100, 100, 400, 300)

        label1 = QLabel("Name")
        name_edit = QLineEdit()

        label2 = QLabel("Age")
        age_edit = QLineEdit()

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        form_layout.addRow(label1, name_edit)
        form_layout.addRow(label2, age_edit)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
