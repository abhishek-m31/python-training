try:
    # fr = open('../Day3/Files/mydata.txt', 'r')

    # print(type(fr))

    with open('../Day3/Files/mydata.txt', 'r') as fr:

    data = fr.read()

    print(data)



except FileNotFoundError:
    print('File not found')


 
try:
    with open('../Day3/Files/mydata.txt', 'r') as fr:
        lines = fr.readlines()
        print(type(lines)) # list
    for line in lines:
        print(line)
    



except FileNotFoundError:

print('File not found')
 
try:

data = """this is a string
multiline strings can be enclosed in triple quote"""

with open('../Day3/Files/new_data.txt', 'w') as fw:

fw.write(data)

except FileNotFoundError:

print('File not found')
 
try:

books = [['Java 8', '700'], ['Python for beginners', '500'], ['R Programming', '450'], ['AI/ML using Python', '900']]

with open('../Day3/Files/bookdata.txt', 'w') as fw:

for book in books:

fw.writelines(f'{book}\n')

except FileNotFoundError:

print('File not found')
 