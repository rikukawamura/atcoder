def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = 12
x = [[] for i in range(N+1)]
for i in range(1, N+1):
    for j in range(i, N+1, i):
        x[i].append(j)
pdb.set_trace()