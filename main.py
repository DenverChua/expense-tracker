import csv
from datetime import datetime

# File to store expenses
EXPENSES_FILE = "expenses.csv"

def load_expenses():
    """Load expenses from CSV file."""
    expenses = []
    try:
        with open(EXPENSES_FILE, mode="r") as file:
            reader = csv.DictReader(file)
            expenses = list(reader)
    except FileNotFoundError:
        pass  # File doesn't exist yet (first run)
    return expenses

def save_expenses(expenses):
    """Save expenses to CSV file."""
    with open(EXPENSES_FILE, mode="w", newline="") as file:
        fieldnames = ["amount", "category", "date"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense(expenses):
    """Add a new expense."""
    try:
        amount = float(input("Enter amount spent: $"))
        category = input("Enter category (e.g., food, transport): ").strip()
        date = input("Enter date (YYYY-MM-DD) [today]: ").strip()
        date = date if date else datetime.now().strftime("%Y-%m-%d")
        
        expenses.append({"amount": amount, "category": category, "date": date})
        save_expenses(expenses)
        print("✅ Expense added!")
    except ValueError:
        print("❌ Invalid amount. Please enter a number.")

def view_summary(expenses):
    """Show total spending and category breakdown."""
    if not expenses:
        print("No expenses recorded yet.")
        return
    
    total = sum(float(e["amount"]) for e in expenses)
    print(f"\n📊 Total spent: ${total:.2f}")
    
    # Category breakdown
    categories = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + float(e["amount"])
    
    print("\n📂 By category:")
    for category, amount in categories.items():
        print(f"  {category}: ${amount:.2f}")

def view_all_expenses(expenses):
    """Display all expenses in a table."""
    if not expenses:
        print("No expenses found.")
        return
    
    print("\n📝 All expenses:")
    print(f"{'Amount':<10} | {'Category':<15} | {'Date':<10}")
    print("-" * 35)
    for e in expenses:
        print(f"${e['amount']:<9} | {e['category']:<15} | {e['date']:<10}")

def main():
    """Main CLI loop."""
    expenses = load_expenses()
    
    while True:
        print("\n💵 Expense Tracker CLI")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. View All Expenses")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_summary(expenses)
        elif choice == "3":
            view_all_expenses(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()