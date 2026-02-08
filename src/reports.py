from collections import defaultdict

def total_expenses(expenses):
    return sum(e.amount for e in expenses)

def average_expense(expenses):
    return total_expenses(expenses) / len(expenses) if expenses else 0

def category_wise_report(expenses):
    report = defaultdict(float)
    for e in expenses:
        report[e.category] += e.amount
    return report

def save_report(report_data, filename):
    with open(f"reports/{filename}", "w") as file:
        for k, v in report_data.items():
            file.write(f"{k}: {v}\n")