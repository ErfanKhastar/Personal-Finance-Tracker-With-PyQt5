# Personal Finance Tracker
A desktop application for personal finance management, developed using Python and PyQt5. This program allows users to track their income and expenses, set budgets, and view detailed reports on their financial status.

<br>

## ✨ Features
* **User Authentication:** Secure sign-up and login system for multiple users.
* **Main Dashboard:** A summary of your financial status, including total income, total expenses, and current balance.
* **Data Visualization:** A dynamic pie chart displaying the top 5 budget categories for a clear visual breakdown.
* **Transaction Management:** Add, categorize, and view all your income and expense transactions.
* **Budgeting:** Set or recurring budgets for different expense categories.
* **Reporting:** View a detailed report comparing your actual spending against your set budgets.
* **Modern UI:** A clean and user-friendly interface designed with PyQt5 and custom stylesheets.

<br>

## 🛠️ Technologies Used
* **Programming Language:** `Python`
* **GUI Framework:** `PyQt5`
* **Database:** `MySQL`
* **Data Visualization:** `Matplotlib`
* **Database Connector:** `mysql-connector-python`
* **Password Hashing:** `bcrypt`
* **Environment Variables:** `python-dotenv`

<br>

## ⚙️ Setup and Installation
Follow these steps to run the project on your local machine.

### 1. Prerequisites
* **Python 3.8+** installed on your system.
* **MySQL Server** installed and running.

### 2. Clone the Repository
Clone the project from GitHub to your local machine:
```bash
git clone https://github.com/ErfanKhastar/Personal-Finance-Tracker-With-PyQt5.git
cd Personal-Finance-Tracker-With-PyQt5
```

### 3. Install Required Libraries
It is highly recommended to use a virtual environment to manage dependencies.
* The requirements file is in the app's file you can use that.
```bash
pip install -r requirements.txt
```

### 4. Database Setup
The application will automatically create the necessary database and tables on its first run. You only need to provide the connection details for your MySQL server.

### 5. Configure Environment Variables
In the root directory of the project, create a new file named .env. Copy the following template into it and fill it with your MySQL server credentials.
```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=finance
```
* **DB_HOST:** The host of your MySQL server (usually localhost).
* **DB_USER:** Your MySQL username (often root).
* **DB_PASSWORD:** The password for your MySQL user.
* **DB_NAME:** The name of the database the application will create (it's best to leave this as finance).

<br>

## 🚀 How to Run
After completing the setup steps, run the application by executing the **users.py** file:
```bash
python users.py
```
You will need to sign up for a new user account first, then you can log in.


