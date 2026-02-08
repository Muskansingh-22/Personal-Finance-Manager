from .expense import Expense
from .file_manager import save_expenses, load_expenses, backup_data, restore_data
from .reports import total_expenses, average_expense, category_wise_report, save_report
from .utils import get_input, validate_amount, validate_date

def show_menu():
    print("""
====== Personal Finance Manager ======
1. Add Expense
2. View Total Expenses
3. View Average Expense
4. Category-wise Report
5. Backup Data
6. Restore Data
0. Exit
""")

def handle_choice(choice):
    expenses = load_expenses()

    if choice == "1":
        amount = get_input("Amount: ", validate_amount)
        category = get_input("Category: ")
        date = get_input("Date (YYYY-MM-DD): ", validate_date)
        desc = get_input("Description: ")

        expense = Expense(amount, category, date, desc)
        save_expense(expense)
        print("Expense added successfully")

    elif choice == "2":
        print("Total Expenses:", total_expenses(expenses))

    elif choice == "3":
        print("Average Expense:", average_expense(expenses))

    elif choice == "4":
        report = category_wise_report(expenses)
        save_report(report, "category_report.txt")
        print("Category report saved")

    elif choice == "5":
        backup_data()
        print("Backup created")

    elif choice == "6":
        restore_data()
        print("Data restored")
