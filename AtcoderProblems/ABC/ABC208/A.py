def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import product

A, B = int_sp()

if 6*A >= B and B >= 1*A:
    print('Yes')
else:
    print('No')

