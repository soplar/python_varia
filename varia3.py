# updating mutiple state variables
def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print (x)
        t = y
        y = x + y
        x = t

# faster easier
# tuple packing and unpacking
def fibonacci(n):
    x, y = 0, 1
    for i in range(n):
        print (x)
        x, y = y, x + y


