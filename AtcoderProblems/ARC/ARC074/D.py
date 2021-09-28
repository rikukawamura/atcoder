def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import heapq

N = int(input())
A = li_int_sp()

X = A[:N]
heapq.heapify(X)
min_val = heapq.heappop(X)

Y = list(map(lambda x: -x, A[N]))
heapq.heapify(Y)
min_val = heapq.heappop(X)
pdb.set_trace()
for left in range(N+1, 2*N):
    if A[left] > min_val:
        min_val = A[left]
    





