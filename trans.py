Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Initialize an empty list to store transactions
... transactions = []
... 
... # Function to add a transaction
... def add_transaction():
...     date = input("Enter the date (YYYY-MM-DD): ")
...     description = input("Enter a description: ")
...     amount = float(input("Enter the amount: "))
...     transactions.append((date, description, amount))
...     print("Transaction added successfully!")
... 
... # Function to display all transactions
... def display_transactions():
...     if not transactions:
...         print("No transactions recorded.")
...     else:
...         print("\nDate       | Description       | Amount")
...         print("-" * 40)
...         for date, description, amount in transactions:
...             print(f"{date} | {description.ljust(16)} | ${amount:.2f}")
... 
... # Main menu
... while True:
...     print("\nPersonal Finance Tracker")
...     print("1. Add Transaction")
...     print("2. View Transactions")
...     print("3. Exit")
...     
...     choice = input("Enter your choice: ")
...     
...     if choice == "1":
...         add_transaction()
...     elif choice == "2":
...         display_transactions()
...     elif choice == "3":
...         break
...     else:
...         print("Invalid choice. Please try again.")
... 
