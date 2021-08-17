def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, Q = int_sp()
A = li_int_sp()

i = 0
for _ in range(Q):
    T, x, y = int_sp()
    x = x-1
    y = y-1
    i = i%N
    if T == 1:
        A[x-i], A[y-i] = A[y-i], A[x-i]
    elif T == 2:
        i += 1
    elif T == 3:
        print(A[x-i])