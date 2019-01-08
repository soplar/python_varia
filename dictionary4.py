d = {'matthew':'blue', 'rachel':'green', 'raymond':'red'}
# is a dict popitem() atomic? (yes)
while d:
    key, value = d.popitem()
    print (key, '-->', value)

print('-----')
# door popitem is alles weg
print(d)

# The popitem() method removes the item that was last inserted into the dictionary. 


# kijk ook even naar:
# https://docs.python.org/3/library/argparse.html
