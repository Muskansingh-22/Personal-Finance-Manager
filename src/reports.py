from collections import defaultdict
from .file_manager import save_expenses, load_amount_from_expenses, backup_data, restore_data

expenses = load_amount_from_expenses()
amount_list = [float(expense["amount"]) for expense in expenses]
def total_expenses():
    """
    It input list of amount from expenses and return the sum as float.
    """
    return sum(amount_list)

def average_expense():
    """
    Docstring for average_expense
    """
    return round(total_expenses() / len(amount_list),2) if expenses else 0

def category_wise_report(category_to_filter): 
    print(f"Category to Search: {category_to_filter}")
    print("AMOUNT, DATE, DESCRIPTION")
    rows_count = 0
    for data in expenses:
        if data["category"] == category_to_filter:
            rows_count += 1
            print(f"{data['amount'],data['date'],data['description']}")
    if rows_count == 0:
        print("No record found for asked category, Please try different one")
        category_list = [data["category"] for data in expenses]
        category_set = set(category_list)
        print(f"Existing Categories: {category_set}")

def save_report(report_data, filename):
    with open(f"reports/{filename}", "w") as file:
        for k, v in report_data.items():
            file.write(f"{k}: {v}\n")