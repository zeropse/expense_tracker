import sqlite3

# Connect to the database
conn = sqlite3.connect("expenses.db")
cursor = conn.cursor()

# Create the expenses table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        date TEXT,
        amount REAL
    )
""")
conn.commit()

def add_expense(date, amount):
    cursor.execute("INSERT INTO expenses (date, amount) VALUES (?, ?)", (date, amount))
    conn.commit()

def track_expenses():
    total_expenses = 0

    while True:
        date = input("Enter the date (YYYY-MM-DD) or 'q' to quit: ")
        if date.lower() == 'q':
            break
        
        try:
            amount = float(input("Enter the expense amount for {}: ".format(date)))
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
            continue
        
        add_expense(date, amount)
        total_expenses += amount
        print("Expense of ${} added for {}.".format(amount, date))
    
    print("\nExpense Tracking Summary:")
    print("=========================")
    
    cursor.execute("SELECT date, SUM(amount) FROM expenses GROUP BY date")
    expenses_summary = cursor.fetchall()
    
    for date, daily_total in expenses_summary:
        print("{}: Total ${:.2f}".format(date, daily_total))
    
    print("=========================")
    print("Overall Total Expenses: ${:.2f}".format(total_expenses))

if __name__ == "__main__":
    track_expenses()

# Close the database connection
conn.close()
