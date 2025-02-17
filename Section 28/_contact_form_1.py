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
    QTextEdit,
)
import sys
from PyQt6.QtGui import QPixmap, QFont
import math


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Send Message")
        self.setGeometry(100, 100, 400, 300)

        form_layout = QFormLayout()
        self.setLayout(form_layout)

        self.name_edit = QLineEdit()
        self.email_edit = QLineEdit()
        self.phone_edit = QLineEdit()

        self.subject_combo = QComboBox()
        self.subject_combo.addItems(
            ["Select subject", "Personal message", "Bussines message", "Other"],
        )

        self.message_edit = QTextEdit()

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submitClicked)

        form_layout.addRow(QLabel("Name"), self.name_edit)
        form_layout.addRow(QLabel("Email"), self.email_edit)
        form_layout.addRow(QLabel("Phone"), self.phone_edit)
        form_layout.addRow(QLabel("Subject"), self.subject_combo)
        form_layout.addRow(QLabel("Message"), self.message_edit)
        form_layout.addRow(submit_button)

    def submitClicked(self):
        name = self.name_edit.text()
        email = self.email_edit.text()
        phone = self.phone_edit.text()
        subject = self.subject_combo.currentText()
        message = self.message_edit.toPlainText()

        print(
            f"Name: {name}\nEmail:{email}\nPhone; {phone}\nSubject:{subject}\nMessage: {message}\n"
        )
        self.name_edit.clear()
        self.email_edit.clear()
        self.phone_edit.clear()
        self.subject_combo.clear()
        self.message_edit.clear()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
