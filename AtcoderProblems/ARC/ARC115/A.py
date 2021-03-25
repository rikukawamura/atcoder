import pdb
import collections

N, M = map(int, input().split())
S = [int(input(), 2) for _ in range(N)]
S_col = collections.Counter(S)
pdb.set_trace()

for key, value in zip(S_col.keys(), S_col.values()):
    if S_col[-~key] in S_col.keys():
        pdb.set_trace()
        print(key, value)

