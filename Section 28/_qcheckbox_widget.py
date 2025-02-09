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

        sugar_checkbox = QCheckBox(self)
        sugar_checkbox.setText("Sugar")
        sugar_checkbox.move(20, 40)
        sugar_checkbox.toggled.connect(self.sugar_checked)

        self.label = QLabel(self)
        self.label.setText("")
        self.label.resize(200, 20)
        self.label.move(20, 90)

    def sugar_checked(self, checked):
        if checked:
            # print("Sugar added")
            self.label.setText("Sugar added!")
        else:
            # print("No sugar")
            self.label.setText("No sugar.")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
