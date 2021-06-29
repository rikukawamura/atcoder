import itertools
import pdb

N, M = map(int, input().split())
adj_matrix = [[0]* N for _ in range(N)]

for i in range(M): #隣接行列
    a, b = map(int, input().split())
    adj_matrix[a-1][b-1] = 1
    adj_matrix[b-1][a-1] = 1
pdb.set_trace()

# 何通りあるかのカウンター
cnt = 0

for each in itertools.permutations(range(N)):
    pdb.set_trace()
    if each[0] != 0:
        break
    factor = 1
    for i in range(N-1):
        factor *= adj_matrix[each[i]][each[i+1]]
    cnt += factor

print(cnt)