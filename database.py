import bcrypt
import mysql.connector
from dotenv import load_dotenv
import os
from session import Session

load_dotenv()

def connect():
    return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )


def mydb():
    conn = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

    cursor = conn.cursor()

    # Create Database
    cursor.execute("CREATE DATABASE IF NOT EXISTS finance")

    cursor.execute("USE finance")

    # Users Table
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            password VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
            """)

    # Transactions Table
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Transactions(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            category VARCHAR(50),
            amount DECIMAL(10,2),
            type VARCHAR(20),
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES Users(ID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
            )
            """)

    # Budgets Table
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS Budgets(
            ID INT AUTO_INCREMENT PRIMARY KEY,
            user_id INT,
            category VARCHAR(50),
            limit_amount DECIMAL(10,2),
            FOREIGN KEY (user_id) REFERENCES Users(ID)
            ON DELETE CASCADE
            ON UPDATE CASCADE
            )
            """)

    cursor.close()
    conn.close()


def add_user(data: dict):
    conn = connect()
    cursor = conn.cursor()
    query = """
        INSERT INTO Users
        (username, password)
        VALUES (%s, %s)
    """
    values = (
        data["username"],
        data["password"]
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def verify_user(data: dict):
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT password FROM Users WHERE username = %s"
    cursor.execute(query, (data["username"],))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row is None:
        return False

    stored_hash = row[0]
    if isinstance(stored_hash, str):
        stored_hash = stored_hash.encode("utf-8")

    user_password = data["password"].encode("utf-8")

    return bcrypt.checkpw(user_password, stored_hash)


def add_transaction(data: dict):
    conn = connect()
    cursor = conn.cursor()
    query = """
        INSERT INTO Transactions
        (user_id, category, amount, type)
        VALUES (%s, %s, %s, %s)
        """
    values = (
        data["user_id"],
        data["category"],
        data["amount"],
        data["type"]
    )
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def add_budget(data: dict):
    conn = connect()
    cursor = conn.cursor()

    query = """
            INSERT INTO Budgets
            (user_id, category, limit_amount)
            VALUES (%s, %s, %s)
            """

    values = (
        data["user_id"],
        data["category"],
        data["limit_amount"]
    )

    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()


def get_transactions_list():
    conn = connect()
    cursor = conn.cursor()
    query = """
            SELECT category, amount, type, date
            FROM Transactions
            WHERE user_id = %s
            ORDER BY amount DESC
            LIMIT 40
            """
    cursor.execute(query, (Session.user_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def recent_transactions():
    conn = connect()
    cursor = conn.cursor()
    query = """
            SELECT category, amount, type, date
            FROM Transactions
            WHERE user_id = %s
            ORDER BY ID DESC
            LIMIT 5
            """
    cursor.execute(query, (Session.user_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_budgets_list():
    conn = connect()
    cursor = conn.cursor()
    query = """
            SELECT category, limit_amount 
            FROM Budgets
            WHERE user_id = %s
            ORDER BY ID DESC
            LIMIT 20
            """
    cursor.execute(query, (Session.user_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_reports():
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT
            B.category,
            SUM(B.limit_amount) AS total_limit,
            IFNULL(T.total_expense, 0) AS spent,
            (SUM(B.limit_amount) - IFNULL(T.total_expense, 0)) AS diffrence
        FROM Budgets AS B
        LEFT JOIN (
            SELECT category, user_id, SUM(amount) AS total_expense
            FROM Transactions
            WHERE type = "expense"
            GROUP BY user_id, category
        ) AS T ON T.user_id = B.user_id AND T.category = B.category
        WHERE B.user_id = %s
        GROUP BY B.category
        ORDER BY total_limit DESC
    """
    cursor.execute(query, (Session.user_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def total_income():
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT SUM(amount)
    FROM Transactions
    WHERE user_id = %s AND type = "income"
    """
    cursor.execute(query, (Session.user_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row[0]


def total_expense():
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT SUM(amount)
        FROM Transactions
        WHERE user_id = %s AND type = "expense"
        """
    cursor.execute(query, (Session.user_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row[0]


def top_five_budgets():
    conn = connect()
    cursor = conn.cursor()
    query = """
        SELECT category, SUM(limit_amount) AS total_limit
        FROM Budgets
        WHERE user_id = %s
        GROUP BY category
        ORDER BY total_limit DESC
        LIMIT 5
    """
    cursor.execute(query, (Session.user_id,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_current_user_id(username):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT ID FROM Users WHERE username = %s", (username,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row[0]


mydb()
