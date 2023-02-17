import datetime

def subtract_days_from_current_date(num_days):
    # Get the current date
    current_date = datetime.datetime.today()

    # Subtract num_days from the current date
    new_date = current_date - datetime.timedelta(days=num_days)

    # Return the new date
    return new_date.strftime("%Y-%m-%d")

a=subtract_days_from_current_date(5)
print(a)
