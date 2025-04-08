#Global Namespace
#variables are resolved in the order : local -> enclosing -> global -> built-in
import builtins

list = [233, 89, 90] #shadows built-in name 'list'
len = 20
name = 'Gauri'
age = 40

print(builtins.len(name))

def display():
    #local namesapce created
    name = 'Gautam'
    age  = 30
    print(f'Name: {name}\nAge: {age}') #local objects 
    print(globals())
    print(locals())

if __name__  == '__main__': #this runs the module in a script mode only
    display()
    print(f'Name: {name}\nAge: {age}') #global objects