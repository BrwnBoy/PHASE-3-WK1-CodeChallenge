from datetime import datetime

def convert_time(hour, minute, period):
    # Covert the input into a time starting in 12-hour format
    time_str = f'{hour}:{minute:02d} {period.upper()}'
    # Parse the time string into a datetime object
    t = datetime.strptime(time_str, '%I:%M %p')\
    # Format the dateti,e object into a 24-hour time string
    return t.strftime('%H%M')

# Testing of the Function
print(convert_time(8, 30, 'pm'))
print(convert_time(8, 30, 'am'))