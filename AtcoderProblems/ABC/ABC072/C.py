import pdb
from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

B = []
for a in A:
    B.append([a-1, a, a+1])

dd = defaultdict(int)
for x in B:
    for key in x:
        dd[key] += 1
dd = sorted(dd.items(), key=lambda x: x[1], reverse=True)
print(dd[0][1])

