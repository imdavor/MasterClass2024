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
)

import sys
from PyQt6.QtGui import QPixmap, QFont, QAction, QIcon
import math


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 400, 300)

        toolbar = self.addToolBar("Main Toolbar")

        self.file_action = QAction("File")
        self.new_action = QAction(QIcon("icons/file_new_icon.png"), "New")
        self.open_action = QAction(QIcon("icons/open_icon.png"), "Open")
        self.edit_action = QAction("Edit")
        self.save_action = QAction(QIcon("icons/save_icon.png"), "Save")
        self.view_action = QAction("View")

        toolbar.addAction(self.file_action)
        toolbar.addAction(self.new_action)
        toolbar.addAction(self.open_action)
        # toolbar.addSeparator()
        toolbar.addAction(self.edit_action)
        toolbar.addAction(self.save_action)
        toolbar.addAction(self.view_action)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
