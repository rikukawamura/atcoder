import pdb
import copy
import operator
import itertools
import collections


n, k, q = map(int, input().split())
a = [int(input()) for _ in range(q)]
scores = [k-q] * n
a_col = collections.Counter(a)

for key, value in zip(a_col.keys(), a_col.values()):
    scores[key-1] += value
print(*['Yes' if x > 0 else 'No' for x in scores], sep='\n')