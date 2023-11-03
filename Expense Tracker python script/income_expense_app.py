import sqlite3
import tkinter as tk
from tkinter import messagebox

class IncomeExpenseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Income and Expenses Tracker")
        
        self.create_tables()

        self.balance_label = tk.Label(root, text="Current Balance: ₹0.00")
        self.balance_label.pack()

        self.income_entry = tk.Entry(root, width=50)
        self.income_entry.insert(0, "")
        self.income_entry.pack()

        self.income_button = tk.Button(root, text="Enter Income", command=self.enter_income)
        self.income_button.pack()

        self.expense_entry = tk.Entry(root, width=50)
        self.expense_entry.insert(0, "")
        self.expense_entry.pack()

        self.expense_button = tk.Button(root, text="Enter Expense", command=self.enter_expense)
        self.expense_button.pack()

        self.balance_button = tk.Button(root, text="Display Balance", command=self.display_balance)
        self.balance_button.pack()

        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.pack()

    def create_tables(self):
        conn = sqlite3.connect("income_expenses.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                type TEXT,
                amount REAL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def insert_transaction(self, transaction_type, amount):
        conn = sqlite3.connect("income_expenses.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (type, amount)
            VALUES (?, ?)
        """, (transaction_type, amount))
        conn.commit()
        conn.close()

    def get_balance(self):
        conn = sqlite3.connect("income_expenses.db")
        cursor = conn.cursor()
        cursor.execute("""
            SELECT SUM(CASE WHEN type = 'income' THEN amount ELSE -amount END) AS balance
            FROM transactions
        """)
        balance = cursor.fetchone()[0] or 0
        conn.close()
        return balance

    def enter_income(self):
        income = float(self.income_entry.get())
        self.insert_transaction("income", income)
        self.income_entry.delete(0, tk.END)
        self.update_balance_label()

    def enter_expense(self):
        expense = float(self.expense_entry.get())
        self.insert_transaction("expense", expense)
        self.expense_entry.delete(0, tk.END)
        self.update_balance_label()

    def display_balance(self):
        balance = self.get_balance()
        messagebox.showinfo("Balance", f"Current Balance: ₹{balance:.2f}")

    def update_balance_label(self):
        balance = self.get_balance()
        self.balance_label.config(text=f"Current Balance: ₹{balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = IncomeExpenseApp(root)
    root.mainloop()
