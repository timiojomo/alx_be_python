
from datetime import datetime

def display_current_datetime():
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
   

display_current_datetime()

number_of_days = int(input("Enter the number of days "))

def calculate_future_date():
    timedelta = datetime.timedelta(days = number_of_days)
    print(datetime.date.today() + timedelta)

calculate_future_date()