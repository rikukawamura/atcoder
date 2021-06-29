import pdb

N = int(input())
A = list(map(int, input().split()))

min_val = float('INF')
for i in range(2**(N-1)):
    x0 = 0
    xt = 0
    for j in range(N):
        print(j)
        x0 |= A[j]
        if i & (1 << j) or j == N-1:
            xt ^= x0
            x0 = 0
    min_val = min(min_val, xt)
print(min_val)







