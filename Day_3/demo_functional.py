books = [['Java', 700], ['Python for beginners',500 ], ['R programming ', 450]]
print(books)

def by_length(lst):
    return lst[1]

sorted_books = sorted(books)
print(sorted_books)

"""Call by function : by_length
  sent as am argument to another function, it chnages behaviour of calling function"""

sorted_by_price = sorted(books, key=by_length)
print(sorted_by_price)
sorted_by_price = sorted(books, key=lambda lst: lst[1])
print(sorted_by_price)

colors = ['Red','Blue','White','Black','Orange']
def get_length(s):
    return len(s)

colors.sort()
print(colors)

colors.sort(key=get_length)
print(colors)
colors.sort(key=lambda s: len(s))
print(colors)

filtered = list(filter(lambda s: s[0] == 'B', colors))
print(filtered)

mapped = list(map(lambda s: len(s), colors))
print(mapped)

mapped = list(map(lambda s: s.upper(), colors))
print(mapped)

smallest = min(colors, key=lambda s: len(s))
print(smallest)

longest = max(colors, key=lambda s: len(s))
print(longest)


print('-------------------------------')
numbers = [12,34,45, 64, 46, 67,55 , 54,43,65,54]
even_numbers = list(filter(lambda n: n%2 == 0, numbers))
print(even_numbers)

squares = list(map(lambda n: n * n, numbers))
print(squares)


min_num = min(numbers)
print(min_num)
max_num = max(numbers)
print(max_num)

print('--------------------------------------')
books = { 'Java': 700, 'Python for beginners': 500 , 'R programming ': 450}
print(books)

price_filter = dict(filter(lambda item: item[1]))
print(price_filter)

min_price = min(books.items(), key=lambda item: item[1])
print(min_price)

max_price = max(books.items(), key=lambda item: item[1])
print(max_price)