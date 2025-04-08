from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

today = date.today()
print('Today', today)

tommarow = today + timedelta(days=1)
print(tommarow)

yesterday = today - timedelta(days=1)
print(yesterday)

next_week = today + timedelta(weeks=1)
print(next_week)

tommarow = today + relativedelta(days=1)
print(tommarow)

next_month = today + relativedelta(month=1)
print(next_month)

first_of_next__month = today + relativedelta(months=1, day=1)
print(first_of_next__month)

previous_week = today - relativedelta(weeks=1)
print(previous_week)

first_monday_of_next = today + relativedelta(months=1, day=1,weekday=MO )
first_monday_of_previous = today - relativedelta(month=1, day=1, weekday=MO)

time_diff = relativedelta(today, previous_week)
print(time_diff)
