def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import combinations

ABC = li_int_sp()
max_val = 0
for x, y in combinations(ABC, 2):
    max_val = max(max_val, x+y)
print(max_val)

