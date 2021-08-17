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
X = A[:(N*3)//2]
Y = A[(N*3)//2:]

preA = []
for i, x in enumerate(X):
    preA.append([x, i])

lasA = []
for i, y in enumerate(Y, (N*3)//2):
    lasA.append([-y, i])


heapq.heapify(preA)
heapq.heapify(lasA)
for _ in range(N//2):
    heapq.heappop(preA)
    heapq.heappop(lasA)

pre_total = 0
las_total = 0
for i, j in zip(preA, lasA):
    pre_total += i[0]
    las_total += -j[0]
print(pre_total-las_total)