def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import Counter

S = []
for _ in range(4):
    s = input()
    S.append(s)
S = Counter(S)
if len(S) == 4:
    print('Yes')
else:
    print('No')
