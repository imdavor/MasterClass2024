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

        self.total_cost = 0.00

        label = QLabel(self)
        label.setText("Choose option")
        label.resize(200, 20)
        label.move(20, 20)

        # add chekckboxes
        sugar_checkbox = QCheckBox(self)
        sugar_checkbox.setText("Sugar ($ 0.50)")
        sugar_checkbox.move(20, 40)
        sugar_checkbox.toggled.connect(self.sugar_checked)

        milk_checkbox = QCheckBox(self)
        milk_checkbox.setText("Milk ($ 1.00)")
        milk_checkbox.move(20, 60)
        milk_checkbox.toggled.connect(self.milk_checked)

        # display total result
        self.result_label = QLabel(self)
        self.result_label.setText("Total cost: $0.00")
        self.result_label.resize(200, 20)
        self.result_label.move(20, 90)

    def sugar_checked(self, checked):
        if checked:
            self.total_cost += 0.50
        else:
            self.total_cost -= 0.50
        self.result_label.setText("Total cost: $" + str(self.total_cost))

    def milk_checked(self, checked):
        if checked:
            self.total_cost += 1.00
        else:
            self.total_cost -= 1.00
        self.result_label.setText("Total cost: $ " + str(self.total_cost))


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
