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

        open_action = QAction("Open", self)
        file_menu.addAction(open_action)
        open_action.triggered.connect(self.open_file)

        save_action = QAction("Save", self)
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save_file)

        save_as_action = QAction("Save as", self)
        file_menu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_as_file)

        # edit menu
        edit_menu = QMenu("Edit", self)
        menubar.addMenu(edit_menu)

        undo_action = QAction("Undo", self)
        edit_menu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)

        redo_action = QAction("Redo", self)
        edit_menu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)

        edit_menu.addSeparator()

        cut_action = QAction("Cut", self)
        edit_menu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)

        copy_action = QAction("Copy", self)
        edit_menu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)

        paste_action = QAction("Paste", self)
        edit_menu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)

    def new_file(self):
        print("Creating New File")

    def open_file(self):
        print("Opening file")

    def save_file(self):
        print("Saving file")
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "All Files(*);;Python File(*.py)"
        )
        if file_path:
            with open(file_path, "w") as file:
                file.write(self.edit_field.toPlainText())

    def save_as_file(self):
        print("Saving as...")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
