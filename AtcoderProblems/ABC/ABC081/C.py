import pdb
import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))
A_col = collections.Counter(A)
A_col = sorted(A_col.items(), key=lambda x:x[1], reverse=False)

count = 0
for i, x in zip(range(len(A_col)-K), A_col):
    count += x[1]

print(count)
