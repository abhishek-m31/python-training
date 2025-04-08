def outer(func):
    def wrapper():
        print('start')
        func()
        print('End')
    return wrapper   

@outer
def display():
    print('Good Morning')

display()

def smart_math(func):
    def wrapper(*args, **kwargs):
        no1,no2 = args
        if no1 < no2:
            no1, no2 = no2, no1
        func(no1, no2)
    return wrapper      

@smart_math
def divide(n1, n2):
    return n1/n2

print(divide(4, 12))
   


