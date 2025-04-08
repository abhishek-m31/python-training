import os as o

print(o.getcwd())

is_present = o.path.isfile('../Day_3/file/abc.txt')
print(is_present)

is_present = o.path.isdir('../Day_3/file')
print(is_present)

with o.scandir('../Day_2') as entries:
    for entry in  entries:
        if entry.is_file():
            print(entry.name)
        if entry.is_dir():
            print(entry.name)

if not o.path.isdir('../Day_3/Demo'):
    o.mkdir('../Day_3/Demo')   

if o.path.isfile('../Day_3/Demo/test.txt'):   
    o.rename('../Day_3/Demo/test.txt', '../Day_3/Demo/Data.txt')

if o.path.isfile('../Day_3/Demo/Data.txt'):
    o.remove('../Day_3/Demo/Data.txt')

if not o.path.isdir('../Day_3/2025'):
    o.makedirs('../Day3/2025/03/26')

if o.path.isdir('../Day_3/Demo'):
    o.rmdir('../Day_3/Demo')        