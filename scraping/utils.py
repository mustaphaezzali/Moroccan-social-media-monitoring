import re
import datetime

# Define the Arabic and English date format strings
arabic_format = '%A %d %B %Y - %H:%M'
english_format = '%A, %B %d, %Y - %I:%M %p'

# Define the regular expression pattern for the Arabic date
pattern = r'^(\S+)\s+(\d+)\s+(\S+)\s+(\d+)\s*-\s*(\d+):(\d+)$'

# Extract the individual date components using the regular expression
match = re.match(pattern, 'الإثنين 24 أبريل 2023 - 16:00')

# Convert the month name to a number
months = {'يناير': 1, 'فبراير': 2, 'مارس': 3, 'أبريل': 4, 'مايو': 5, 'يونيو': 6, 'يوليو': 7, 'أغسطس': 8, 'سبتمبر': 9, 'أكتوبر': 10, 'نوفمبر': 11, 'ديسمبر': 12}

# Create a datetime object from the date components


def transform(arabic_date):
    match = re.match(pattern, arabic_date)
    day_name, day, month_name, year, hour, minute = match.groups()
    month = months[month_name]
    date_object = datetime.date(int(year), month, int(day))
    return date_object


