import re
message = 'Good Morning! Hav a Good day'

span = re.search(r'Good', message)
print(span)
print(span.start())
print(span.end())

matches = re.findall(r'Good', message)
print(matches)

my_str = '.zip, sip, rip, ripe, tip, lip, ship, ip, wip.'
pattern = re.compile('[a-z]?ip') #3 or 2 - letter words ending with ip
words = re.findall(pattern, my_str)
print(words)

words = re.findall('[a-z]+ip', my_str) #min 3 letter words ending with ip
print(words)

words = re.findall('[a-z]*ip', my_str)
print(words)

words = re.findall('[a-m]+ip', my_str)
print(words)

print('-------------------------------')
if re.search(r'^zip', my_str):
    print('Starts with zip')
if re.search(r'wip$', my_str):
    print('Ends with wip')

matches = re.findall('\.', my_str)
print(matches)
