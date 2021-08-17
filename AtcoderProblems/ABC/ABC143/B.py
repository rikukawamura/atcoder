def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import combinations

N = int(input())
D = li_int_sp()
total = 0
for i, j in combinations(D, 2):
    total += i*j
print(total)
