def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

A, B, C, D = int_sp()
if A <= C <= B or A <= D <= B or (C < A and D > B) :
    print('Yes')
else:
    print('No')