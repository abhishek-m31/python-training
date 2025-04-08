try:
    try:
        fr = open('../Day_3/file/abc.txt', 'r')
        data = fr.read(10)
        print(data)
    
    finally:
        fr.close()
except FileNotFoundError as er:
    print(er)    


try:
    #open('../Day_3/files/mydata.txt', 'r')
    #print(type(fr))
    with open('../Day_3/file/abc.txt', 'r') as fr:
        data = fr.read(3)

except FileNotFoundError:
    print('File not found')       

try:
    #open('../Day_3/files/mydata.txt', 'r')
    #print(type(fr))
    with open('../Day_3/file/abc.txt', 'r') as fr:
        lines = fr.readlines()
        print(type(lines))
        for line in lines:
            print(line)

except FileNotFoundError:
    print('File not found')   

try:
    #open('../Day_3/files/mydata.txt', 'r')
    #print(type(fr))
    with open('../Day_3/file/abc.txt', 'w') as fw:
        data = fw.write(data)

except FileNotFoundError:
    print('File not found')       

    