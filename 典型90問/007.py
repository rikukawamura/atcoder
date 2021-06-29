def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb
from math import log
import bisect


N = int(input())
A = sorted(li_int_sp())
Q = int(input())
#pdb.set_trace()
#print(300000 * log(300000, 2))

def compare(N):
    return N <= b

output = []
if N == 1:
    for _ in range(Q):
        output.append(abs(A[0]-int(input())))

    for i in output:
        print(i)
    exit()

for _ in range(Q):
    #pdb.set_trace()
    b = int(input())
    index = bisect.bisect_left(A, b)
    if index == 0:
        output.append(abs(b - A[index]))
    elif index == N:
        output.append(abs(b - A[index-1]))
    else:
        output.append(min(abs(b-A[index-1]), abs(b-A[index])))

for i in output:
    print(i)

