import pdb
import numpy as np


from itertools import accumulate

C = 200005  # 累積和の配列の長さCです。適当に200000より大きい数にしておきます。

N, W = map(int, input().split())
seq_a = [0] * C

for _ in range(N):
    s, t, p = map(int, input().split())
    seq_a[s] += p
    seq_a[t] -= p

S = list(accumulate(seq_a))

if max(S) <= W:
    print('Yes')
else:
    print('No')
'''
N, W = map(int, input().split())
S, T, P = list(map(list, (zip(*[list(map(int, input().split())) for _ in range(N)]))))
max_T = max(T)
graph = np.array([[0]*max_T for _ in range(N)])


i = 0
for s, t, p in zip(S, T, P):
    np.put(graph, range(i+s-1, i+t-1), p)
    i+=max_T
sum_graph = np.max(np.sum(graph, axis=0))
#pdb.set_trace()
if sum_graph <= W:
    print('Yes')
else:
    print('No')
'''