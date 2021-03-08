import pdb
import itertools


# itertools.groupbyを使う例として分かりやすい問題
n = int(input())
s = input()
s_group = itertools.groupby(s)

cn = 0
for i, j in s_group:
    cn += 1
print(cn)