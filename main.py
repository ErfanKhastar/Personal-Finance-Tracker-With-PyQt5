from PyQt5 import uic
from PyQt5.QtWidgets import (
    QMainWindow, QWidget,
    QPushButton, QLabel, QLineEdit, QMessageBox,
    QStackedWidget, QTableView, QComboBox,
    QVBoxLayout, QAbstractItemView
    )
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from decimal import Decimal
import database
from datetime import datetime
from session import Session
from add_transaction import AddTransactionUI

class MainUI(QMainWindow):
    def __init__(self):
        super().__init__()


        # Load The UI File
        uic.loadUi("main.ui", self)
        # Set the app's title
        self.setWindowTitle("Personal Finance Tracker")


        # Define Our Widgets
        # Sidebar Buttons
        self.dashboardButton = self.findChild(QPushButton, "dashboardButton")
        self.transactionsButton = self.findChild(QPushButton, "transactionsButton")
        self.budgetsButton = self.findChild(QPushButton, "budgetsButton")
        self.reportsButton = self.findChild(QPushButton, "reportsButton")


        # Stackedwidgets
        self.stackedWidget = self.findChild(QStackedWidget, "stackedWidget")
        self.dashboardPage = self.findChild(QWidget, "dashboardPage")
        self.transactionsPage = self.findChild(QWidget, "transactionsPage")
        self.budgetsPage = self.findChild(QWidget, "budgetsPage")
        self.reportsPage = self.findChild(QWidget, "reportsPage")


        # Dashboard Page
        self.addTransactiondButton = self.findChild(QPushButton, "addTransactiondButton")
        self.helloLabel = self.findChild(QLabel, "helloLabel")
        self.dateLabel = self.findChild(QLabel, "dateLabel")
        self.incomeLabel = self.findChild(QLabel, "incomeLabel")
        self.expenseLabel = self.findChild(QLabel, "expenseLabel")
        self.balanceLabel = self.findChild(QLabel, "balanceLabel")
        self.expensesCategoryLabel = self.findChild(QLabel, "expensesCategoryLabel")
        self.recentTransactionstableView = self.findChild(QTableView, "recentTransactionstableView")
        self.chartLayout = self.findChild(QVBoxLayout, "chartLayout")


        # Transactions Page
        self.addTransactiontButton = self.findChild(QPushButton, "addTransactiontButton")
        self.transactionsLabel = self.findChild(QLabel, "transactionsLabel")
        self.transactionstableView = self.findChild(QTableView, "transactionstableView")


        # Budgets Page
        self.budgetsLabel = self.findChild(QLabel, "budgetsLabel")
        self.addbudgetlabel = self.findChild(QLabel, "addbudgetlabel")
        self.categorylabel = self.findChild(QLabel, "categorylabel")
        self.categorycomboBox = self.findChild(QComboBox, "categorycomboBox")
        self.amountlabel = self.findChild(QLabel, "amountlabel")
        self.amountlineEdit = self.findChild(QLineEdit, "amountlineEdit")
        self.savebudgetButton = self.findChild(QPushButton, "savebudgetButton")
        self.editbudgetButton = self.findChild(QPushButton, "editbudgetButton")
        self.budgetstableView = self.findChild(QTableView, "budgetstableView")


        # Reports Page
        self.reportsLabel = self.findChild(QLabel, "reportsLabel")
        self.reportstableView = self.findChild(QTableView, "reportstableView")


        # Stylesheet for TableVeiws
        self.transactionstableView.setAlternatingRowColors(True)
        self.transactionstableView.setStyleSheet("""
                    QTableView {
                        background-color: #f5f0e6;
                        alternate-background-color: #e9e0d1;
                        gridline-color: #a47551;
                        outline: none;
                        color: #3e2c1c;
                        selection-background-color: #d1bfa5;
                        selection-color: #000;
                        border: 1px solid #a47551;
                        font-size: 16px;
                        font-family: "Arad Medium"
                    }
                    QHeaderView::section {
                        background-color: #a47551;
                        color: white;
                        padding: 5px;
                        border: 1px solid #c1a37b;
                        font-size: 18px;
                        font-family: "Arad Medium"
                    }
                    """)

        self.recentTransactionstableView.setAlternatingRowColors(True)
        self.recentTransactionstableView.setStyleSheet("""
                    QTableView {
                        background-color: #f5f0e6;
                        alternate-background-color: #e9e0d1;
                        gridline-color: #a47551;
                        color: #3e2c1c;
                        selection-background-color: #d1bfa5;
                        selection-color: #000;
                        border: 1px solid #a47551;
                        font-size: 16px;
                        font-family: "Arad Medium"
                    }
                    QHeaderView::section {
                        background-color: #a47551;
                        color: white;
                        padding: 5px;
                        border: 1px solid #c1a37b;
                        font-size: 18px;
                        font-family: "Arad Medium"
                    }
                    QTableView#recentTransactionstableView QTableCornerButton::section {
                        background-color: #a47551;
                        border: 1px solid #c1a37b;
                    }
                    """)

        self.budgetstableView.setAlternatingRowColors(True)
        self.budgetstableView.setStyleSheet("""
                    QTableView {
                        background-color: #f5f0e6;
                        alternate-background-color: #e9e0d1;
                        gridline-color: #a47551;
                        outline: none;
                        color: #3e2c1c;
                        selection-background-color: #d1bfa5;
                        selection-color: #000;
                        border: 1px solid #a47551;
                        font-size: 16px;
                        font-family: "Arad Medium"
                    }
                    QHeaderView::section {
                        background-color: #a47551;
                        color: white;
                        padding: 5px;
                        border: 1px solid #c1a37b;
                        font-size: 18px;
                        font-family: "Arad Medium"
                    }
                    """)

        self.reportstableView.setAlternatingRowColors(True)
        self.reportstableView.setStyleSheet("""
                    QTableView {
                        background-color: #f5f0e6;
                        alternate-background-color: #e9e0d1;
                        gridline-color: #a47551;
                        outline: none;
                        color: #3e2c1c;
                        selection-background-color: #d1bfa5;
                        selection-color: #000;
                        border: 1px solid #a47551;
                        font-size: 16px;
                        font-family: "Arad Medium"
                    }
                    QHeaderView::section {
                        background-color: #a47551;
                        color: white;
                        padding: 5px;
                        border: 1px solid #c1a37b;
                        font-size: 18px;
                        font-family: "Arad Medium"
                    }
                    """)


        # Don't let user to edit the data that's in the tables
        edit_trigger = QAbstractItemView.NoEditTriggers
        self.transactionstableView.setEditTriggers(edit_trigger)
        self.recentTransactionstableView.setEditTriggers(edit_trigger)
        self.budgetstableView.setEditTriggers(edit_trigger)
        self.reportstableView.setEditTriggers(edit_trigger)


        # Stylesheet for ComboBox (Budgets page)
        self.categorycomboBox.setStyleSheet("""
                    QComboBox {
                        border: 2px solid #A47551;
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

        self.categorycomboBox.view().setStyleSheet("""
                    QAbstractItemView {
                        background-color: #f5f0e6;
                        color: #3e2c1c;
                        selection-background-color: #e0d1bd;
                        selection-color: #3e2c1c;
                        border: 1px solid #A47551;
                    }
                """)


        # Connect functions to the buttons
        self.dashboardButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.transactionsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.budgetsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.reportsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.addTransactiondButton.clicked.connect(self.open_transaction_window)
        self.addTransactiontButton.clicked.connect(self.open_transaction_window)
        self.savebudgetButton.clicked.connect(self.add_budget)


        # Set default text and add items (Budgets page)
        self.amountlineEdit.setPlaceholderText("Enter amount...")
        self.categorycomboBox.insertItem(0, "Select a category...")
        self.categorycomboBox.setCurrentIndex(0)
        self.categorycomboBox.addItems([
            "Work", "Food", "Shopping", "Gym",
            "Car", "Travel", "Party", "Transport",
            "Resturant", "Game", "School", "University",
            "Home Stuff", "Junk Food"
                                        ])

        # Get The Date
        today = datetime.today()
        formatted_date = today.strftime("%B %d, %Y")
        self.dateLabel.setText(formatted_date)


        # Put user's name on the label
        self.helloLabel.setText(f"Hello, {Session.username}")


        # Fill the labels Income, Expense, balance
        income = database.total_income()
        expense = database.total_expense()
        if income is None:
            income = Decimal("0.00")
        if expense is None:
            expense = Decimal("0.00")
        self.incomeLabel.setText(f"INCOME\n{income}")
        self.expenseLabel.setText(f"EXPENSE\n{expense}")
        self.balanceLabel.setText(f"BALANCE\n{income - expense}")


        # Add the data into tables
        self.load_recent_transactions()

        self.load_transactions()

        self.load_budgets()

        self.load_reports()


        # Show pie chart for top five budget's category
        self.show_budgets_pie_chart()


        # Show The App
        self.show()


    def open_transaction_window(self):
        self.transaction_window = AddTransactionUI()
        self.transaction_window.transaction_added.connect(self.update_dashboard)


    def update_dashboard(self):
        income = database.total_income()
        expense = database.total_expense()
        if income is None:
            income = Decimal("0.00")
        if expense is None:
            expense = Decimal("0.00")
        self.incomeLabel.setText(f"INCOME\n{income}")
        self.expenseLabel.setText(f"EXPENSE\n{expense}")
        self.balanceLabel.setText(f"BALANCE\n{income - expense}")
        self.load_recent_transactions()
        self.load_transactions()
        self.load_reports()
        self.show_budgets_pie_chart()


    def load_transactions(self):
        transactions = database.get_transactions_list()

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Category", "Amount", "Type", "Date"])

        for row in transactions:
            items = []
            for feild in row:
                item = QStandardItem(str(feild))
                item.setTextAlignment(Qt.AlignCenter)
                items.append(item)
            model.appendRow(items)

        self.transactionstableView.setModel(model)

        self.transactionstableView.resizeColumnsToContents()
        self.transactionstableView.horizontalHeader().setStretchLastSection(True)

        self.transactionstableView.verticalHeader().setDefaultSectionSize(58)
        self.transactionstableView.horizontalHeader().setDefaultSectionSize(100)

        self.transactionstableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)


    def load_recent_transactions(self):
        transactions = database.recent_transactions()

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Category", "Amount", "Type","Date"])

        for row in transactions:
            items = []
            for feild in row:
                item = QStandardItem(str(feild))
                item.setTextAlignment(Qt.AlignCenter)
                items.append(item)
            model.appendRow(items)

        self.recentTransactionstableView.setModel(model)

        self.recentTransactionstableView.resizeColumnsToContents()
        self.recentTransactionstableView.horizontalHeader().setStretchLastSection(True)

        self.recentTransactionstableView.verticalHeader().setDefaultSectionSize(58)
        self.recentTransactionstableView.horizontalHeader().setDefaultSectionSize(110)

        self.recentTransactionstableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)


    def load_budgets(self):
        budgets = database.get_budgets_list()

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Category", "Limit Amount"])

        for row in budgets:
            items = []
            for feild in row:
                item = QStandardItem(str(feild))
                item.setTextAlignment(Qt.AlignCenter)
                items.append(item)
            model.appendRow(items)

        self.budgetstableView.setModel(model)

        self.budgetstableView.resizeColumnsToContents()
        self.budgetstableView.horizontalHeader().setStretchLastSection(True)

        self.budgetstableView.verticalHeader().setDefaultSectionSize(58)
        self.budgetstableView.horizontalHeader().setDefaultSectionSize(100)

        self.budgetstableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)


    def load_reports(self):
        reports = database.get_reports()

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Category", "Limit Amount", "Spent", "Diffrence"])

        for row in reports:
            items = []
            for value in row:
                item = QStandardItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                items.append(item)
            model.appendRow(items)

        self.reportstableView.setModel(model)

        self.reportstableView.resizeColumnsToContents()
        self.reportstableView.horizontalHeader().setStretchLastSection(True)

        self.reportstableView.verticalHeader().setDefaultSectionSize(58)
        self.reportstableView.horizontalHeader().setDefaultSectionSize(140)

        self.reportstableView.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)


    def add_budget(self):
        category = self.categorycomboBox.currentText().strip()
        limit_amount = self.amountlineEdit.text().strip()

        try:
            if limit_amount:
                amount_check = float(limit_amount)
        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Amount must be a number!")
            return

        if category == "Select a category...":
            QMessageBox.warning(self, "Warning", "Please select a category.")
            return

        if not limit_amount:
            QMessageBox.warning(self, "Warning", "Please enter amount part.")
            return

        data = {
            "user_id": Session.user_id,
            "category": category,
            "limit_amount": limit_amount
        }

        try:
            database.add_budget(data)
            QMessageBox.information(self, "Success", "Budget Added.")
            self.amountlineEdit.setText("")
            self.categorycomboBox.setCurrentIndex(0)
            self.load_budgets()
            self.load_reports()
            self.show_budgets_pie_chart()
        except Exception as e:
            QMessageBox.warning(self, "ERORR!", str(e))


    def show_budgets_pie_chart(self):
        if self.chartLayout:
            for i in reversed(range(self.chartLayout.count())):
                widget = self.chartLayout.itemAt(i).widget()
                if widget is not None:
                    widget.setParent(None)

        data = database.top_five_budgets()

        if not data:
            no_data_label = QLabel("No budget data to display.\nPlease add a budget.")
            no_data_label.setAlignment(Qt.AlignCenter)
            no_data_label.setStyleSheet("font-family: 'Arad Medium'; font-size: 18px; color: #888;")
            self.chartLayout.addWidget(no_data_label)
            return

        categories = [row[0] for row in data]
        values = [float(row[1]) for row in data]

        figure = Figure(figsize=(5,5), dpi=100)
        figure.patch.set_facecolor("#f5f0e6")
        canvas = FigureCanvas(figure)
        ax = figure.add_subplot(111)
        ax.set_facecolor("#f5f0e6")

        ax.pie(values, labels=categories, startangle=140,
               textprops={"color": "#3e2c1c", "fontsize": 10})

        fig = plt.gcf()
        fig.gca().add_artist(plt.Circle((0, 0)))

        ax.axis("equal")
        plt.tight_layout()

        self.chartLayout.addStretch()
        self.chartLayout.addWidget(canvas)
        self.chartLayout.addStretch()

