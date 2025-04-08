emp_data= {'name': 'Abhishek',
           'age' : 22,
           'dept': 'IT',
           'salary': 500000,
           'skills': ['Java','Python','Javascript']}

weather_data= {'mumbai' : 32,
               'Pune' : 30,
               'Banglore': 36,
               'Delhi': 35 }

name = emp_data['name']
print(name)

skills = emp_data['skills']
print('java' in skills)


print('--------------------------')
for city in weather_data.keys():
    print(city, '--', weather_data[city])

print('---------------------------')
for x, y in weather_data.items():
    print(x, '---', y)

print('------------------------')
for val in weather_data.values():
    print(val)

print('---------------------')
emp_data['age'] = 33
print(emp_data)

emp_data['city'] = 'Pune'
print(emp_data)

weather_data.update({'Chennai' : 39})
print(weather_data)

weather_data.pop('Chennai')
print(weather_data)

print(weather_data.get('Pune'))
