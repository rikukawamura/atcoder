import pdb
import itertools

N = int(input())
T = [int(input()) for _ in range(N)]

min_time = float('INF')
for bit in range(2**N):
    A = []
    B = []
    for i in range(N):
        if 1 & (bit >> i):
            A.append(T[i])
        else:
            B.append(T[i])
    #print(A, B)
    tmp_time = max(sum(A), sum(B))
    if tmp_time < min_time:
        min_time = tmp_time
print(min_time)


