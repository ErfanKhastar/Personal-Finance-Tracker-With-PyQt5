from PyQt5 import uic
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QPushButton, QLabel, QLineEdit, QMessageBox
    )
import sys
from new_user import NewuserUI
from main import MainUI
import database
from session import Session


class UsersUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load The UI File
        uic.loadUi("users.ui", self)
        # Set the app's title
        self.setWindowTitle("Login")

        # Define Our Widgets
        self.usernamelabel = self.findChild(QLabel, "usernamelabel")
        self.userpasswordlabel = self.findChild(QLabel, "userpasswordlabel")
        self.usernameLineEdit = self.findChild(QLineEdit, "usernameLineEdit")
        self.userpasswordLineEdit = self.findChild(QLineEdit, "userpasswordLineEdit")
        self.loginButton = self.findChild(QPushButton, "loginButton")
        self.signupButton = self.findChild(QPushButton, "signupButton")

        # Connect functions to the buttons
        self.loginButton.clicked.connect(self.login)
        self.signupButton.clicked.connect(self.signup)

        # Show The App
        self.show()

    # Open "Sign Up" window
    def signup(self):
        self.signup_window = NewuserUI()

    # Open "Login" window
    def login(self):
        username = self.usernameLineEdit.text().strip()
        password = self.userpasswordLineEdit.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Missing Fields", "Please enter both username and password!")
            return

        data = {
            "username": username,
            "password": password
        }

        try:
            is_valid = database.verify_user(data)

            if is_valid:
                QMessageBox.information(self, "Success", "User Logged In!")

                Session.set(database.get_current_user_id(username), username)

                self.main_window = MainUI()
                self.close()
            else:
                QMessageBox.warning(self, "Login Failed", "Invalid username or password!")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UsersUI()
app.exec_()
