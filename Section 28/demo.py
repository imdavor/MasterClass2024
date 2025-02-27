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
    QComboBox,
    QStackedLayout,
    QVBoxLayout,
    QTextEdit,
    QMenuBar,
    QMenu,
    QFileDialog,
    QInputDialog,
)
import sys
from PyQt6.QtGui import QPixmap, QFont, QAction, QIcon, QTextCursor, QColor
from PyQt6.QtCore import Qt
import math


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(100, 100, 400, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
