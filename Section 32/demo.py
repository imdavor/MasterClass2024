from PyQt6.QtWidgets import (
    QWidget,
    QMainWindow,
    QApplication,
    QStyleFactory,
    QLabel,
    QVBoxLayout,
    QPushButton,
)
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0, 0, 700, 500)

        label = QLabel("<h1>This is label</h1>", self)
        label.resize(200, 50)
        label.setStyleSheet(
            """
        background-color:gray; 
        color:white;
        margin:100px;
        """
        )

        button = QPushButton("Click Here!")
        button.setStyleSheet(
            """
        QPushButton{
            background-color:gray;
            padding: 5px;
        }
        QPushButton:pressed{
            background-color:blue;
            padding: 5px;
        }    
        """
        )
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)


app = QApplication(sys.argv)
# app.setStyle("Fusion")
window = Window()
print(QStyleFactory.keys())
print(app.style().name())

window.show()
sys.exit(app.exec())
