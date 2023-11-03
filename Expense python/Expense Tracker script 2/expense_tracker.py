def main():
    # Create an empty dictionary to store expenses
    expenses = {}
    
    while True:
        print("Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            amount = float(input("Enter amount: "))
            description = input("Enter description: ")
            
            if date in expenses:
                expenses[date].append({"amount": amount, "description": description})
            else:
                expenses[date] = [{"amount": amount, "description": description}]
            
            print("Expense added successfully!")
            
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD) to view expenses: ")
            if date in expenses:
                print(f"Expenses on {date}:")
                for expense in expenses[date]:
                    print(f"Amount: ₹{expense['amount']:.2f}, Description: {expense['description']}")
            else:
                print("No expenses found for this date.")
            
        elif choice == "3":
            print("Exiting the Expense Tracker.")
            break
            
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
