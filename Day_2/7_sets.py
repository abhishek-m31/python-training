colors = {'Red','Blue','White','Black','Orange'}
colors1 = {'Pine','Violet','Indigo','Black','Red','Orange'}
print(colors)

print(id(colors))
print(type(colors))
colors.add('Yellow')

for color in colors:
    print(color)

print('Red' in colors)
print('Pink' not in colors)    

print('-------------Set Methodsd-------------')
colors.add('Yellow')
print(colors)
"""remove vs Discard both removes element but remove gives an error if item is not present"""
colors.remove('Yellow')
print(colors)
colors.discard('Yellow')
print(colors)

print(colors.pop()) #gives any random item form set
colors.update(['Pink', 'Violet'])
print(colors)

print('-------------Set Operations--------------')
colorset = colors.union(colors1)
print(colorset)

colorset = colors | colors1
print(colorset)

colorset = colors.intersection(colors1)
print(colorset)

colorset = colors & colors1
print(colorset)

colorset= colors.difference(colors1)
print(colorset)

colorset= colors - colors1
print(colorset)