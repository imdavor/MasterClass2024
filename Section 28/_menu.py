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
from PyQt6.QtGui import QPixmap, QFont, QAction
import math


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Menu")
        self.setGeometry(100, 100, 400, 300)

        # step 1 create manu bar
        menubar = self.menuBar()

        # creating menu
        file_menu = menubar.addMenu("File")
        edit_menu = menubar.addMenu("Edit")

        # creating an Action
        self.new_action = QAction("New")

        self.exit_action = QAction("Exit")

        self.copy_action = QAction("Copy")
        self.cut_action = QAction("Cut")
        self.paste_action = QAction("Paste")

        # adding Action to the Menu
        file_menu.addAction(self.new_action)
        # add separator
        file_menu.addSeparator()
        file_menu.addAction(self.exit_action)

        edit_menu.addAction(self.copy_action)
        edit_menu.addAction(self.cut_action)
        edit_menu.addAction(self.paste_action)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
