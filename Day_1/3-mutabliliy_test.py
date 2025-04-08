"""Immutable vs Mutable data types :
For an immutable data type if two objects have same value they are same objects in memory
identity operator 'is' will always return True
Any modification to value creates a new Object instead of modifying the same one
For a mutable data type even if two objects have same value they are not same objects in memory
identity operator 'is' will never always return True
Any modification to value doesn't create a new Object instead it modifies the same one"""

a = 10
b = 10
print(id(a))
print(id(b))

if a is b:
    print('Same Objects')

lst1 = [11, 12]
lst2 = [11, 12] 
print(id(lst1))
print(id(lst2))

if lst1 is lst2:
    print('Same Objects')

lst3 = lst1 #copy referance
if lst1 is lst3:
    print('Same Objects')    