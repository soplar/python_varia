names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']
# let op er is één kleur meer dan namen
# construct a dictionary
d = dict(enumerate(names))
print(d)

print('----')

# construct a dictionary from pairs
# in python3 doet zip hetzelfde als izip in python2
d = dict(zip(names, colors))
print(d)
print('----')

# counting with dictionaries
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1
print(d)
print('----')

# eenvoudiger
d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1
print(d)
print('----')

# moderner
from collections import defaultdict
d = defaultdict(int)
for color in colors:
    d[color] += 1
print(d)


