import csv

def ViewExpenses():
    """
    Reads and displays all expense records from the CSV file.
    Ensures that each row has the correct format and skips malformed rows.
    """
    with open("budget-tracker-info.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3: 
                try:
                    print(f"date: {row[0]}      description: {row[1]}       amount: ${float(row[2]):.2f}")
                except ValueError:
                    print(f"Skipping malformed amount in row: {row}")
            else:
                print(f"Skipping malformed row: {row}")

def AddBudget():
    """
    Prompts the user to enter the date, description, and amount for a new expense.
    Validates the amount input and appends the record to the CSV file.
    """
    date = input("What is the date? ")
    description = input("What is this for? ")
    try:
        amount = float(input("How much is it? (Enter a positive or negative number): "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    with open("budget-tracker-info.csv", "a") as file:
        writer = csv.DictWriter(file, fieldnames=["date", "description", "amount"])
        writer.writerow({"date": date, "description": description, "amount": amount})

def ViewBudget():
    """
    Calculates and displays the total balance by summing up all amounts in the CSV file.
    Skips rows with malformed or invalid amounts.
    """
    budget = 0.0
    with open("budget-tracker-info.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) == 3:
                try:
                    budget += float(row[2])
                except ValueError:
                    print(f"Skipping malformed amount in row: {row}")
    print(f"Total balance: ${budget:.2f}")

def main():
    """
    Provides a menu for the user to interact with the budget tracker.
    Options include adding a new expense, viewing all expenses, and viewing the total balance.
    """
    try:
        system = int(input("Enter 1 to add a new expense, 2 to view expenses, 3 to view balance: "))
    except ValueError:
        print("Invalid input. Please enter 1, 2, or 3.")
        return

    match system:
        case 1:
            AddBudget()
        case 2:
            ViewExpenses()
        case 3:
            ViewBudget()
        case _:
            print("Invalid option. Exiting...")

if __name__ == "__main__":
    main()
