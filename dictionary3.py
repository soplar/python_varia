names = ['raymond', 'rachel', 'matthew', 
         'roger', 'betty', 'melissa',
         'judith', 'charlie']
# groeperen op lengte of op voorletter f aantal t's
d = {}
for name in names:
    # key = len(name)
    # key = name[0]
    key = name.count('t')
    if key not in d:
        d[key] = []
    d[key].append(name)
print(d)
print('-----------')
# sneller
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)
print(d)
print('-----------')
# nieuwer en sneller
from collections import defaultdict
d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
print(d)
print('-----------')
