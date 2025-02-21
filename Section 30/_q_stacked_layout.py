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
from PyQt6.QtGui import QPixmap, QFont
import math


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(100, 100, 400, 300)

        combo_box = QComboBox()
        combo_box.addItems(["Label", "Form"])
        combo_box.activated.connect(self.change_page)

        # creating page 1
        label = QLabel("This is LABEL page")

        # creating page 2
        form = QFormLayout()
        form.addRow("", QLabel("This is form page"))
        page2_container = QWidget()
        page2_container.setLayout(form)

        # create stacked layout
        self.stacked_layout = QStackedLayout()
        self.stacked_layout.addWidget(label)
        self.stacked_layout.addWidget(page2_container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(combo_box)
        main_layout.addLayout(self.stacked_layout)

        self.setLayout(main_layout)

    def change_page(self, index):
        self.stacked_layout.setCurrentIndex(index)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
