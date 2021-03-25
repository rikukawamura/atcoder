import pdb
from collections import Counter
from collections import defaultdict
import itertools
from operator import mul
from functools import reduce

# 考え方は最初からOK
# combinationsの高速化をすると通った
def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

n = int(input())
s = [str(Counter(sorted(list(input())))) for _ in range(n)]


#　要素の数をカウント
dic = Counter(s)

count = 0
for i in dic.keys():
    if dic[i] > 1:
        count += cmb(dic[i], 2)
print(count)