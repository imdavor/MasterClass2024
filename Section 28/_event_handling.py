from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import sys
from PyQt6.QtGui import QPixmap, QFont


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.count = 0
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0, 0, 400, 300)

        # new code for button
        button = QPushButton(self)
        button.setText("Click Me")
        button.move(160, 100)
        button.clicked.connect(self.buttonClicked)

        # adding label do display count
        self.label = QLabel(self)
        self.label.setText("0")
        self.label.move(195, 80)

    def buttonClicked(self):
        # print("You clicked ME!!!")
        self.count += 1
        self.label.setText(str(self.count))
        self.label.adjustSize()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
