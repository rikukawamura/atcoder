def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, A, X, Y = int_sp()

total = 0
for i in range(1, N+1):
    if i > A:
        total+=Y
    else:
        total+=X
print(total)
