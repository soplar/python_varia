p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'
# variabelen vullen
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]
# unpacking sequences
fname2, lname2, age2, email2 = p

print(lname)
print('--------------')
print(lname2)