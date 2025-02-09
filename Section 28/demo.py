from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QLabel,
    QPushButton,
    QLineEdit,
    QCheckBox,
)
import sys
from PyQt6.QtGui import QPixmap, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0, 0, 400, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
