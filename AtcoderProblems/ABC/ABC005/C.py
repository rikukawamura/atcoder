def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from bisect import bisect_left
T = int(input())
N = int(input())
A = li_int_sp()
M = int(input())
B = li_int_sp()

if M > N:
    print('no')
    exit()

cnt = 0
for b in B:
    #pdb.set_trace()
    x = bisect_left(A, b)
    for i in reversed(range(2)):
        try:
            if b-A[x-i] <= T and b-A[x-i] >= 0:
                cnt += 1
                del A[x-i]
                break
        except IndexError:
            continue

if cnt == M:
    print('yes')
else:
    print('no')

