my_string = 'Python is a dynamic language'

print(my_string)
print(id(my_string))
lower = my_string.lower()
print(id(lower))

if 'Python' in my_string:
    print('Present')

if 'java' not in my_string:
    print('Not present')

print('---------------Indexing and slicing----------------------')   
print(my_string[8])
print(my_string[-3])
print(my_string[2:12])
print(my_string[12:2])  #empty String if dtart index > end-index
print(my_string[-10:-2])
print(my_string[3:20:2])
print(my_string[3:20:-2]) #negative stride : reverse the indices
print(my_string[20:3:-2]) #string in reverse order
print(my_string[:5] + my_string[5:])
print(my_string[::-1])  #reverse string


print('----------------------Case Conversion-------------------')
print(my_string.lower())
print(my_string.upper())
title = my_string.title()
print(title)
swapped = my_string.swapcase()
print(swapped)
print(my_string.capitalize())


print('------------------Char Classification--------------')
value = 'hello'
print(value.isalpha())
value = '2234'
print(value.isdecimal())
value = '\u00B223'
print(value.isdigit())
value = '676\u2168'
print(value.isnumeric())
value = '676\u2168add'
print(value.isalnum())
value = 'i1_val'
print(value.isidentifier())


print('-----------------Other Methods---------------')
words = 'fox, box, rox, tox, nox, ox'
print(words.count('ox'))
print(words.find('box'))
print(words.replace('ox', 'at'))
lst = words.split(', ')
print(lst)


newstr = '-'.join(lst)
print(newstr)


message = '   Welcome !! Hope you are doing well   '
print(message.strip())
parts = message.partition('Hope')
print(parts)

print(message.strip().startswith('welcome'))
print(message.strip().endswith('well'))

msg = "Welcome !! Hope you are doing well"

if message.strip() == msg:
    print('Equal')


