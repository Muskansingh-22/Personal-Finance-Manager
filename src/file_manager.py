import csv
import os
from .expense import Expense 

DATA_FILE = "data/expenses.csv"

def load_amount_from_expenses():
    
    if not os.path.exists(DATA_FILE):
        return "No old entries exist"
    
    with open(DATA_FILE, mode="r", newline="") as expense_file:
        reader = csv.DictReader(expense_file)
        next(reader, None)
        expense_dict = [row for row in reader]
    return expense_dict

def save_expenses(expense):
    file_exists = os.path.exists(DATA_FILE)
    with open(DATA_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["amount", "category","date","description"])
        writer.writerow(expense.to_list())

def backup_data():
    import shutil
    shutil.copy(DATA_FILE, "data/expenses_backup.csv")

def restore_data():
    import shutil
    shutil.copy("data/expenses_backup.csv", DATA_FILE)