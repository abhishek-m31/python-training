def increment(no):
    no +=1
    return no

func = increment(23) #function call
print(func)

func = increment #assigning func to variable
print(func(34))

add_val = lambda n: n + 1 #shorthand notation to create anonymous functions
print(add_val(20))

l1 = lambda x, y, z : x+y+z
print(l1(10, 12, 10))

l2 = lambda x, y, z=5 : x+y+z
print(l2(12,10))

l3 = lambda *args: sum(args)
print(l3(2,3,4,55,5,6))

l4 = lambda **kwargs: sum(kwargs.values())
print(l4(one=1, two=2, three=3))