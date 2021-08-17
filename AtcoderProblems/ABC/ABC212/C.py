def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from math import log
from bisect import bisect_right

N, M = int_sp()
A = sorted(li_int_sp())
B = li_int_sp()
#print((2*10**5)+log(2*10**5))
min_val = float('INF')
for b in B:
    #pdb.set_trace()
    b_ind = bisect_right(A, b)
    if b_ind == 0:
        min_val = min(min_val, abs(b-A[0]))
    elif b_ind == N:
        min_val = min(min_val, abs(b-A[N-1]))
    else:
        min_val = min(min_val, abs(b - A[b_ind - 1]))
        min_val = min(min_val, abs(b - A[b_ind]))
print(min_val)



