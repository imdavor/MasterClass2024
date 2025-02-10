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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0, 0, 400, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
