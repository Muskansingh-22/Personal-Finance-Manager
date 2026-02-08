class Expense:
    def __init__(self, amount, category, date, descrption):
        self.amount = float(amount)
        self.category = category
        self.date = date
        self.description = descrption
    
    def to_list(self):
        return[self.amount, self.category, self.date, self.description]