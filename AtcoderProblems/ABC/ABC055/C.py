import pdb
import math

N, M = map(int, input().split())

if N >= M/2:
    print(math.floor(M/2))
    exit()

c_remain = M - (N*2)
c_only = math.floor(c_remain / 4)

print(N+c_only)
