from PyQt6.QtWidgets import QWidget, QApplication
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My firs PyQt Window")
        self.setGeometry(0, 0, 400, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
