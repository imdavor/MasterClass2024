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
        button = QPushButton("Show message", self)
        button.setGeometry(150, 80, 200, 40)
        button.clicked.connect(self.show_Message_Box)

    def show_Message_Box(self):
        msg = QMessageBox()
        msg.setWindowTitle("Message box Title")
        msg.setText("This is simple message!")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel
        )
        msg.setDefaultButton(QMessageBox.StandardButton.Ok)
        result = msg.exec()

        if result == QMessageBox.StandardButton.Ok:
            print("Ok button clicked")
        else:
            print("Cancel button clicked")


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
