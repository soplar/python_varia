# list comprehensions and generator expressions
result = []
for i in range(10):
    s = i ** 2
    result.append(s)
print (sum(result))

print('--------------')
# a single comprehensive line of thought

print (sum([i**2 for i in range(10)]))

print('--------------')
# beter en sneller
print (sum(i**2 for i in range(10)))