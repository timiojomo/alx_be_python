import datetime

def display_current_datetime():

    current_date = datetime.datetime.now()
    print(current_date.isoformat())
   

display_current_datetime()