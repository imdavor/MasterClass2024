from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6.QtGui import QPixmap, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My first PyQt Window")
        self.setGeometry(0, 0, 400, 400)

        with open("car.png"):
            image_label = QLabel(self)
            pixmap = QPixmap("car.png")
            image_label.setPixmap(pixmap)
            image_label.move(50, 0)

        # car name
        name_label = QLabel(self)
        name_label.setFont(QFont("Arial", 20))
        name_label.setText("My Car")
        name_label.move(170, 170)

        # Engine specs
        engine_label = QLabel(self)
        engine_label.setFont(QFont("Arial", 16))
        engine_label.setText("Engine Capacity: 4L TFSI")
        engine_label.move(20, 210)
        # Features
        features_label = QLabel(self)
        features_label.setFont(QFont("Arial", 16))
        features_label.setText("Features: ABS, EBD, ADAS")
        features_label.move(20, 240)
        # Models
        models_label = QLabel(self)
        models_label.setFont(QFont("Arial", 16))
        models_label.setText("Models: 2.2 Diesel, 1.8 Petrol")
        models_label.move(20, 270)
        # Pricing
        pricing_label = QLabel(self)
        pricing_label.setFont(QFont("Arial", 16))
        pricing_label.setText("Pricing: $45,000")
        pricing_label.move(20, 300)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
