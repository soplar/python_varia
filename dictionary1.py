# Looping over dictionary keys
d = {'raymond':'blue', 'rachel':'green', 'matthew':'red'}

for k in d:
    print(k)
# looping over keys and values
for k in d:
    print(k, '-->', d[k])
# als je de values noig hebt, let op items genereert grote lijst
for k, v in d.items():
    print(k, '-->', v)
# betere oplossing: iterator
# let op iteritems wordt niet meer ondersteund in python3
for k, v in iter(d.items()):
    print(k, '-->', v)



# gebruik niet de keys uit het voorbeeld in video
# die retournert een iterator
# gebruik list
for k in list(d):
    if k.startswith('r'):
        del d[k]
print('----')
for k in d:
    print(k)