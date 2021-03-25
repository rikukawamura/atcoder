import pdb
from collections import Counter


N = int(input())
S = Counter([input() for _ in range(N)])
M = int(input())
T = Counter([input() for _ in range(M)])

kinds = set(S+T)
#pdb.set_trace()

min = -float('INF')
for i in kinds:
    getted = S[i] - T[i]
    if getted > min:
        min = getted

if min > 0:
    print(min)
else:
    print(0)




