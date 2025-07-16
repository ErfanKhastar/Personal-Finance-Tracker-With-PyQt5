from PyQt5 import uic
from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox
    )
import bcrypt
import database
from mysql.connector import IntegrityError


class NewuserUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # Load The UI File
        uic.loadUi("new_user.ui", self)
        # Set the app's title
        self.setWindowTitle("Sign Up")

        # Define Our Widgets
        self.newusernamelabel = self.findChild(QLabel, "newusernamelabel")
        self.newuserpasswordlabel = self.findChild(QLabel, "newuserpasswordlabel")
        self.newusernameLineEdit = self.findChild(QLineEdit, "newusernameLineEdit")
        self.newuserpasswordLineEdit = self.findChild(QLineEdit, "newuserpasswordLineEdit")
        self.adduserButton = self.findChild(QPushButton, "adduserButton")

        # Connect function to the button
        self.adduserButton.clicked.connect(self.create_user)

        # Show The App
        self.show()


    def create_user(self):
        username = self.newusernameLineEdit.text().strip()
        password = self.newuserpasswordLineEdit.text().strip()

        if not username or not password:
            QMessageBox.warning(self, "Missing Fields", "Please fill in both fields!")
            return

        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

        data = {
            "username": username,
            "password": hashed_password
        }

        try:
            database.add_user(data)
            QMessageBox.information(self, "Sign Up", "User created successfully!\nNow you can log in.")
            self.close()

        except IntegrityError as e:
            if "Duplicate entry" in str(e):
                QMessageBox.warning(self, "Duplicate entry", "User already exists!")
            else:
                QMessageBox.critical(self, "Database Erorr!", str(e))

        except Exception as e:
            QMessageBox.critical(self, "ERORR!", str(e))


