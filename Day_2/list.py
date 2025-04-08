words = ['sit', 'fit', 'chit', 'bit', 'nit', 'git']

print(words)
if 'git' in words:
    print('present')

if 'got' not in words:
    print('not present')

for item in words:
    print(item.upper())

print('-----------INdexing and slicing-------------')
print(words[2])
print(words[1:5])
print(words[2:10])
print(words[5:1])
print(words[-4])
print(words[-5:-1])
print(words[1:5:1])
print(words[5:1:-1])
print(words[::-1])

print('----------------Methods-----------------')
words[2] = 'fit'  # overwrites ast specific postions
print(words)
words[2:4] = ['wit', 'pit']
print(words)

words.append('bit')
print(words)

words.insert(5, 'rit')
print(words)

words.remove('rit') #value error if item is not present
print(words)

print(words.index('sit'))

print(words.count('fit'))

print(words.pop(3))

words.reverse()
print(words)

words.sort(reverse = True)
print(words)


print('----------------------------')
for x, y in enumerate(words): #returns ordinal]
    print(x, '-', y) 

#append vs extend
words.append(['bit', 'sit'])
print(words)

for item in words:
    if isinstance(item, list): #type comparison operator
        for i in item:
            print(i)
    else:
        print(item)    

words.extend(['wit', 'chit'])
print(words)

numbers = [[1,2,3], [2,3,4], [3,4,5], [4,5,5]] 
for i, j, k in numbers:  #list unpacking 
    print(i, ",", j, ',', k)

print('--------------------List Comprehension-------------------')
sq = []
for a in range(1, 11):
    sq.append(a * a)
print(sq)

square = [a * a for a in range(1, 11)]
print(square)

def calculate_discount(price):
    return price * 0.8

discount_price = []
prices = [200, 900, 230, 870, 980, 340, 870, 450]
for p in prices:
    discount_price.append(calculate_discount(p))
print(discount_price)   

discounted = [calculate_discount(p) for p in prices]
print(discounted)
