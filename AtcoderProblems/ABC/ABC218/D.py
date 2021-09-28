def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

import pdb
import math
from collections import defaultdict
from itertools import combinations
#print(combinations_count(2000, 4))
same_x = defaultdict(list)
N = int(input())
xy = [li_int_sp() for _ in range(N)]
xy = sorted(xy, reverse=False, key=lambda x: x[1])
xy = sorted(xy, reverse=False, key=lambda x: x[0])
#pdb.set_trace()

for x, y in xy:
    same_x[x].append(y)
#pdb.set_trace()

comb = []
for value in same_x.values():
    if len(value) > 1:
        comb.append(combinations(value, 2))

pdb.set_trace()
same_y = defaultdict(lambda: defaultdict(int))
for i in comb:
    for j in i:
        same_y[j[0]][j[1]] += 1
pdb.set_trace()
    
