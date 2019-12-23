import json
import calendar
from collections import Counter

with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

    months = [birthdays[person].split('/')[0] for person in birthdays]
    months_names = [calendar.month_name[int(month)] for month in months]

    c = Counter(months_names)

    print(dict(c))
