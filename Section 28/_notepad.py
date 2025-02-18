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
)
import sys
from PyQt6.QtGui import QPixmap, QFont, QAction, QIcon
import math


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Notepad")
        self.setGeometry(100, 100, 400, 300)

        self.edit_field = QTextEdit(self)
        self.setCentralWidget(self.edit_field)

        # create menubar
        menubar = QMenuBar()
        menubar.setNativeMenuBar(False)  # samo za Mac
        self.setMenuBar(menubar)

        # create menu in menubar
        file_menu = QMenu("File", self)
        menubar.addMenu(file_menu)  # add to menubar

        # create menu item in menu
        # create actions
        new_action = QAction("New", self)
        file_menu.addAction(new_action)
        new_action.triggered.connect(self.new_file)

    def new_file(self):
        print("Creating New File")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
