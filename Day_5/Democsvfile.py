import csv

try:
    with open('../Day_5/files/students.csv', 'r') as fr:
        reader = csv.reader(fr)
        print(type(reader.__next__())) #list
        for row in reader:
            print(row) #list
            print('-'.join(row)) #String
            print(row[0])
except FileNotFoundError as er:
    print(er)

print('-----------------------------------')
try:
    with open('../Day_5/files/students.csv', 'r') as fr:
        reader = csv.DictReader(fr)
        #print(type(reader.__next>>())) #dict
        for row in reader:
            print(row)
            print(f'{row["Name"]}, {row["Marks"]}')
except FileNotFoundError as er:
    print(er)      

print('--------------------------------')
try:
    with open('../Day_5/books.csv', 'w', newline='') as fw:
        data = books = [['Java 8', 700], ['Python for begineers', 500], ['R Programming', 450],['AI/ML using Python', 900]]
        writer = csv.writer(fw)
        for row in data:
            writer.writerow(row)
except FileNotFoundError as er:
    print(er)


print('-------------------------------------')

try:
    with open('../Day_5/files/students.csv', 'r') as fr, open('../Day_5/files/students_new.csv', 'w', newline='') as fw :
    reader = csv.DictReader(fr)
    header = ['Name', 'Marks']
    writer - csv.DictWriter(fw, fieldnames=header)
    writer.writeheader()
    for row in reader:
        writer.writerow(row)
except FileNotFoundError as er:
    print(er)        