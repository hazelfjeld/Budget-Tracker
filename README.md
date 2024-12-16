# Budget-Tracker

A simple budget tracker that allows you to add expenses, view your budget, and view your expenses.

## Features
- Add new expenses with details like date, description, and amount.
- View a complete list of all recorded expenses.
- Calculate and display the total balance of all transactions.
- Handles invalid or malformed data gracefully.

## Technologies Used
- **Python**: The core programming language used for the script.
- **CSV module**: For reading from and writing to the CSV file.

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Clone or download this repository.
2. Ensure a CSV file named `budget-tracker-info.csv` exists in the same directory as the script with the following header:
   ```csv
   date,description,amount
3. Run the script using the following command:
   ```bash
   python budget_tracker.py
## Example Usage

### Adding an Expense
```plaintext
Enter 1 to add a new expense, 2 to view expenses, 3 to view balance: 1
What is the date? 2024-12-15
What is this for? Groceries
How much is it? (Enter a positive or negative number): -50
```

### Viewing Expenses
```plaintext
Enter 1 to add a new expense, 2 to view expenses, 3 to view balance: 2

date: 2024-12-15      description: Groceries       amount: $-50.00
```
### Viewing Balance
```plaintext
Enter 1 to add a new expense, 2 to view expenses, 3 to view balance: 3
Total balance: $-50.00
```
