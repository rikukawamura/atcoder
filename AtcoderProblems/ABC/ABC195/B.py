import pdb
import copy

A, B, W = map(int, input().split())
m = float('INF')
M = 0
for n in range(1, 10**6+1):
    if  (A*n <= 1000*W and 1000*W <= B*n):
        m = min(m,n)
        M = max(M,n)

if M == 0:
    print('UNSATISFIABLE')
else:
    print(m, M)





