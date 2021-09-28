def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import groupby
S = input()
out = []
for key, value in groupby(S):
    #pdb.set_trace()
    out.append(key)
    out.append(str(len(list(value))))
print(''.join(out))
