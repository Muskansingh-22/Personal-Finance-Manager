from datetime import datetime

def validate_amount(amount):
    try:
        value = float(amount)
        if value <= 0:
            raise ValueError
        return value
    except ValueError:
        print ("Invalid amount.")
        return None
    
def validate_date(date_text):
    try:
        datetime.strptime(date_text,"%Y-%m-%d")
        return date_text
    except ValueError:
        print("Date must be YYYY-MM-DD")
        return None
    
def get_input(prompt, validator=None):
    value = input(prompt)
    if validator:
        validated = validator(value)
        if validated is not None:
            return validated
    else:
        return value