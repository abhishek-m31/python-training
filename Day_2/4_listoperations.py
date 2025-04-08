booklist = [['java 8', 700],['Python for Beginners', 500], ['go', 600],['c', 300]]

booklist.append(['cpp', 400])
booklist.remove(['c', 300])
print(booklist)

def by_name(my_list):
    return my_list[0]

def by_price(my_list):
    return my_list[1]

sorted_by_names_ = sorted(booklist, key=by_name)
print(sorted_by_names_)

sorted_by_price = sorted(booklist, key= by_price)
print(sorted_by_price)


max_price= max(booklist, key=lambda book: book[1])
min_price= min(booklist, key=lambda book: book[1])

