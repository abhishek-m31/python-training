weekday = ('sunday', 'monday', 'tuesday', 'wednesday', 'thusrday', 'friday', 'saturday')
print(type(weekday))
print(id(weekday))
print(weekday)

print(weekday[1])

for day in weekday:
    print(day)

print('tuesday' in weekday)
print('thursday' not in weekday) 

lst = list(weekday)
lst.append('Friday')
weekday = tuple(lst)
print(weekday)
print(id(weekday))

lst = list(weekday)
lst.remove('wednesday')
weekday = tuple(lst)
print(weekday)

sorted_wk = sorted(weekday)
print(sorted_wk)

d1,d2, d3, d4, d5, d6, d7 = weekday
print(d2)