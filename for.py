for i in [0,1,2,3,4,5]:
    print(i**2)


# let op in python 2 gebruik je xrange (oude iterator)
# range (in python 3) pakt getal na getal(dus geen gigantischer reservering van geheugen)
for i in range(10):
    print(i)


# gebruik van array
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(colors[i])
# simpel, duidelijker, sneller
for color in colors:
    print(color)

# aflopend
for i in range(len(colors)-1, -1, -1):
    print(colors[i])
# sneller
for color in reversed(colors):
    print(color)

for i in range(len(colors)):
    print(i, '-->', colors[i])
# sneller
for i, color in enumerate(colors):
    print(i, '-->', color)


# enumerate over twee collections
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i])
# beter, sneller en minder geheugen
# in python2 maakt meer gebruik van geheugen (maakt extra tupel)
# gebruik in python2 izip
for name, color in zip(names, colors):
    print(name, '-->', color)

# looping sorted order
colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
    print(color)
# loop backwards
for color in sorted(colors, reverse=True):
    print(color)

# custom sort order
colors = ['red', 'green', 'blue', 'yellow']
# oude manier in python2
# sorteren op basis van lengte van woord
# def compare_length(c1, c2):
#    if len(c1) < len(c2): return -1
#    if len(c1) > len(c2): return 1
#    return 0
# print(sorted(colors, cmp=compare_length))
# python3 mbv key function
print(sorted(colors, key=len))