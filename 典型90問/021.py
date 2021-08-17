def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


import pdb
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import connected_components
from collections import Counter
from math import factorial

N, M = int_sp() # ノード数，エッジ数
edge = np.array([input().split() for _ in range(M)], dtype = np.int64).T
tmp = np.ones(M, dtype = np.int64).T
graph = csr_matrix((tmp, (edge[:] -1)), (N, N)) # 隣接行列を作成
#print(graph)
output = Counter(list((connected_components(graph, directed = True, connection = 'strong'))[1]))
pdb.set_trace()
total = 0
for i in output.values():
    if i > 1:
        total += comb(i, 2)
print(total)


