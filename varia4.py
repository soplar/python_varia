# concatenating strings
names = ['raymond', 'rachel', 'matthew', 'roger', 
         'betty', 'melissa', 'judith', 'charlie']

s = names[0]
for name in names[1:]:
    s += ', ' + name
print (s)


print ('-------------')
# beter
print (', '.join(names))

print ('-------------')
# updating sequences
# wrong way
del names[0]
names.pop(0)
names.insert(0, 'mark')
print (names)

print ('-------------')

# bij grote aantallen duurt dat heel lang
# gebruik andere data structure (deque)
# veel efficienter
from collections import deque
names = deque(['raymond', 'rachel', 'matthew', 'roger', 
         'betty', 'melissa', 'judith', 'charlie'])
del names[0]
names.popleft()
names.appendleft('mark')
print (names)

print ('-------------')
# maak van deque een list
my_list_names = list()
for name in names:
    my_list_names.append(name)

print (my_list_names)

print ('-------------')