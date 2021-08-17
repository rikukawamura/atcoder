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
    #pdb.set_trace()
    T, x, y = int_sp()
    print(A)
    x = x-1
    y = y-1
    i = i%(N-1)
    if T == 1:
        if x+i >= 0 and y+i >= 0:
            A[x-i], A[y-i] = A[y-i], A[x-i]
        elif x-i >= 0 and y-i < 0:
            A[x-i], A[-(y-i+1)] = A[-(y-i+1)], A[x-i]
        elif x-i < 0 and y-i >= 0:
            A[-(x-i+1)], A[y-i] = A[y-i], A[-(x-i+1)]
        else:
            A[-(x-i+1)], A[-(y-i+1)] = A[-(y-i+1)], A[-(x-i+1)]
    elif T == 2:
        i += 1
    elif T == 3:
        if x-i >= 0:
            print(A[x-i])
        else:
            print(A[-(x-i)])