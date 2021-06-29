import pdb
import collections

n = int(input())
S = [input().strip() for _ in range(n)]

cols = []
for s in S:
    cols.append(collections.Counter(s))

keys = []
for col in cols:
    for key in col.keys():
        keys.append(key)

keys = set(keys)

x = collections.defaultdict()

for key in keys:
    tmp = []
    for col in cols:
        tmp.append(col[key])
    x[key] = min(tmp)

x = sorted(x.items())
string = ''
for i in x:
    string += i[0]*i[1]
print(string)



