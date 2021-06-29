import pdb
import numpy as np




N, M = map(int, input().split())
AB = np.array([[0]*N for _ in range(N)])

for _ in range(M):
    a, b = map(int, input().split())
    AB[a-1][b-1] = 1
    AB[b-1][a-1] = 1


pdb.set_trace()