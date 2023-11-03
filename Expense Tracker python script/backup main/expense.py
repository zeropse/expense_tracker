import sqlite3

def create_tables():
    conn = sqlite3.connect("income_expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY,
            type TEXT,  -- 'income' or 'expense'
            amount REAL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_transaction(transaction_type, amount):
    conn = sqlite3.connect("income_expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transactions (type, amount)
        VALUES (?, ?)
    """, (transaction_type, amount))
    conn.commit()
    conn.close()

def get_balance():
    conn = sqlite3.connect("income_expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(CASE WHEN type = 'income' THEN amount ELSE -amount END) AS balance
        FROM transactions
    """)
    balance = cursor.fetchone()[0] or 0
    conn.close()
    return balance

def main():
    print("Daily Income and Expenses Tracker")
    print("--------------------------------")

    create_tables()

    while True:
        print("\nOptions:")
        print("1. Enter Income")
        print("2. Enter Expense")
        print("3. Display Balance")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            income = float(input("Enter income amount: "))
            insert_transaction("income", income)
            print(f"Income of ₹{income:.2f} added.")
        elif choice == "2":
            expense = float(input("Enter expense amount: "))
            insert_transaction("expense", expense)
            print(f"Expense of ₹{expense:.2f} subtracted.")
        elif choice == "3":
            balance = get_balance()
            print(f"Current Balance: ₹{balance:.2f}")
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
