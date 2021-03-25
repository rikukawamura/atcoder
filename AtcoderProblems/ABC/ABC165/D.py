import pdb
import math

A, B, N = map(int, input().split())


if N < B:
    x = math.floor((A*N)/B) - (A*math.floor(N/B))
    print(x)
else:
    x = math.floor((A * (B-1)) / B) - (A * math.floor((B-1) / B))
    print(x)