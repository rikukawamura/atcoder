def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import permutations
S, K = input().split()
#S = list(S)
K = int(K)
dicts = list(permutations(S))
dicts2 = []
for i in dicts:
    i = ''.join(list(i))
    dicts2.append(i)
#pdb.set_trace()
dicts2 = list(set(dicts2))
dicts2.sort()

print(dicts2[K-1])
