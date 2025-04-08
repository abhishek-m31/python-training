def simple_function():
    print('This is a simple function')

simple_function()
def addition (n1, n2):
    print("addition: ", n1 + n2)

addition(4, 6)    
def greater_number(a, b):
    if a > b:
        return a
    else:
        return b    
    
greater = greater_number(12, 24)
print(greater)

addition('one', 'two')
addition([1,2], [3,4])

def increment_salary(name='abhishek', salary='10000'):
    salary += salary * 1

    print(f'New salary for {name} is {salary}')
"""Postional arguments : both datatype and order matters
   Keyword arguments : only data type matters not  the order
   default paramters : assign default value to the parameters"""

increment_salary('Abhi', 40000)
increment_salary(salary=300000, name='naman')    
increment_salary()
increment_salary('prat')
increment_salary(50000) #consider as the first arg

def add_numbers(*number):
    res = 0
    print(type(number))
    for no in number:
        res += no
    print(res)


add_numbers(1,3,4,5,6,6,7)
nos =[1,3,4,5,6,6,7] 

add_numbers(*nos)

def calculate_ave(**data):
    total = 0
    print(data)
    for m in data['marks']:
        total +=m
    ave = total/len(data['marks'])  
    print(f'Average of marks for {data["name"]} is {round(ave, 2)}')  


student_data = {'name' : 'Rucha',
                'marks': [78,90,80]}

calculate_ave(**student_data)    
calculate_ave(name='Rudra', marks=[90, 88, 92, 95])
