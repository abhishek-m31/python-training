import re
rule = 'a-z A-Z #$%^&**( 0-9'

has_digits= re.findall('\d', rule)
print(has_digits)

has_alphanum = re.findall('\w', rule)
print(has_alphanum)

has_special_symbols= re.findall('\W', rule)
print(has_special_symbols)

has_space = re.findall('\s', rule)
print(has_space)

product_data = """
iPhone 8 678905
iPhone 14 987687
iPhone 15 345674
Samsung S8 234567"""

pattern = '\d{6}'
prod_ids = re.findall(pattern, product_data)
print(prod_ids)

pattern = 'iphone\d+'
iphone_data = re.findall(pattern, product_data)
print(iphone_data)

pattern = '\d{6}'
data = re.split(pattern, product_data)
for item in data:
    print(item.strip())


my_date = '2025-03-28  06:02:37'
date_parts = re.split('\W', my_date)
print(my_date)

my_date = re.sub('-', '/', my_date)
print(my_date)