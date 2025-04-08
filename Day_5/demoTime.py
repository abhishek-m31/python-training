import time as tm
from datetime import datetime, time, date

time_stamp = tm.time()
print(time_stamp)

now = datetime.fromtimestamp(time_stamp)
print(now)

today = date(year=2025, month=3, day=28)
print(today)

current_time = time(hour=14, minute=15, second=00)
print(current_time)

dt = datetime.combine(today, current_time)
print(dt)

my_dt = "2024-01-01"#ISO standard format yyyy-mm-dd

my_date = datetime.fromisoformat(my_dt)
print(my_date)

my_dt = "2020/04/01 12:30:30"
my_date = datetime.strptime(my_dt, '%Y/%m/%d %H:%M:%S') #string to datetime
print(my_date)

#strftime : date to string
print(my_date.strftime('%A'))
print(my_date.strftime('%b'))
print(my_date.strftime('%w'))
print(my_date.strftime('%Y'))
print(my_date.strftime('%d-%B-'))



