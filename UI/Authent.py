import sys
import PySide6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFormLayout



class LoginForm(QWidget):
    def __init__(self, *args, **kwargs):
        super(). __init__(*args, **kwargs)
        self.setWindowTitle("Login Form")

        layout = QFormLayout()
        self.setLayout(layout)


        layout.addRow("Username: ", QLineEdit())
        layout.addRow("Password: ", QLineEdit())

        layout.addRow(QPushButton("Login"))

        layout.addRow(QPushButton("Cancel"))
        
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_form = LoginForm()
    login_form.show()
    sys.exit(app.exec())


        








