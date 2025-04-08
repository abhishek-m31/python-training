from dateutil import tz
from datetime import datetime
import zoneinfo
from dateutil.relativedelta import relativedelta
time_zones = zoneinfo.available_timezones()

today = datetime.now()
print(today)

ist = datetime.now(tz=tz.local())
print(ist)
print(ist.tzname())
print(ist.tzinfo)

chicago= tz.gettz('America/Chicago')

uct=datetime.now(tz=chicago)
print(uct)
print(uct.tzname())

ist_local = ist.replace(tzinfo = None)
ch_local = uct.replace(tzinfo=None)

time_diff = relativedelta(ist_local, ch_local)
print(f'time diff : {time_diff.hours} hours, {time_diff.minutes} minutes')

diwali = datetime.fromisoformat('2025-10-20')
