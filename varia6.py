# factor out temporary contexts
from decimal import *
old_context = getcontext().copy()
getcontext().prec = 50
print (Decimal(355) / Decimal(113))
setcontext(old_context)

print('--------------------')


# eenvoudiger
with localcontext(Context(prec = 50)):
    print (Decimal(355) / Decimal(113))

# how to open and close files
# old
f = open('sample.txt')
try:
    data = f.read
finally:
    f.close

# nieuw
with open('sample.txt') as f:
    data = f.read()

# how to use locks
import threading
lock = threading.Lock()

# old way
lock.acquire()
try:
    print ('Critical section 1')
    print ('Critical section 2')
finally:
    lock.release()

# new way
with lock:
    print ('Critical section 1')
    print ('Critical section 2')


# factor-out temporary contexts
import os
try:
    os.remove('verwijder.2.txt')
except OSError:
    pass

# betere oplossing
# create ignored (zie video)
# with ignored(OSError):
#    os.remove('verwijder.1.txt')