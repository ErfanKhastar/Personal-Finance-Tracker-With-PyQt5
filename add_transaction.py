from PyQt5 import uic
from PyQt5.QtWidgets import (
    QMainWindow, QPushButton, QLabel, QLineEdit, QMessageBox,
    QRadioButton, QComboBox
    )
from PyQt5.QtCore import pyqtSignal
from session import Session
import database


class AddTransactionUI(QMainWindow):

    transaction_added = pyqtSignal()

    def __init__(self):
        super().__init__()

        # Load The UI File
        uic.loadUi("add_transaction.ui", self)
        # Set the app's title
        self.setWindowTitle("Add Transaction")

        # Define Our Widgets
        self.categorylabel = self.findChild(QLabel, "categorytlabel")
        self.amountlabel = self.findChild(QLabel, "amountTlabel")
        self.categorytcomboBox = self.findChild(QComboBox, "categorytcomboBox")
        self.amountlineEdit = self.findChild(QLineEdit, "amountTlineEdit")
        self.addTransactiondButton = self.findChild(QPushButton, "addTransactiondButton")
        self.incomeradioButton = self.findChild(QRadioButton, "incomeradioButton")
        self.expenseradioButton = self.findChild(QRadioButton, "expenseradioButton")

        # Click The Button
        self.addTransactiondButton.clicked.connect(self.addtransaction)

        # Stylesheet for ComboBox
        self.categorytcomboBox.setStyleSheet("""
            QComboBox {
                border-radius: 10px;
                padding: 6px;
                background-color: #bfa391;
                color: #3e2c1c;
                font-family: "Arad Medium";
            }

            QComboBox::drop-down {
                image: url("D:/Python/Projects/GitHub_PR/Personal Finance Tracker/down-arrow-8-128.png");
                border: none;
                width: 15px;
                margin-right: 5px;
            }
        """)

        self.categorytcomboBox.view().setStyleSheet("""
            QAbstractItemView {
                background-color: #f5f0e6;
                color: #3e2c1c;
                selection-background-color: #e0d1bd;
                selection-color: #3e2c1c;
                border: 1px solid #A47551;
            }
        """)

        # Set default text and add items
        self.amountlineEdit.setPlaceholderText("Enter amount...")
        self.categorytcomboBox.insertItem(0, "Select a category...")
        self.categorytcomboBox.setCurrentIndex(0)
        self.categorytcomboBox.addItems([
            "Work", "Food", "Shopping", "Gym",
            "Car", "Travel", "Party", "Transport",
            "Resturant", "Game", "School", "University",
            "Home Stuff", "Junk Food"
        ])


        # Show The App
        self.show()


    def addtransaction(self):
        category = self.categorytcomboBox.currentText().strip()
        amount = self.amountlineEdit.text().strip()

        try:
            if amount:
                amount_check = float(amount)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Amount must be a number!")
            return

        if category == "Select a category...":
            QMessageBox.warning(self, "Warning", "Please select a category.")
            return

        if not amount:
            QMessageBox.warning(self, "Warning", "Please enter amount part.")
            return

        if self.incomeradioButton.isChecked():
            type = "income"
        elif self.expenseradioButton.isChecked():
            type = "expense"
        else:
            QMessageBox.warning(self, "Error", "Please select an option")
            return

        data = {
            "user_id": Session.user_id,
            "category": category,
            "amount": amount,
            "type": type
        }

        try:
            database.add_transaction(data)
            QMessageBox.information(self, "Success", "Transaction added.")
            self.transaction_added.emit()
            self.close()

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))


