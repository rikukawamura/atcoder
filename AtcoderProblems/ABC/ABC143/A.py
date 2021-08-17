def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
A, B = li_int_sp()
if A-B*2 > 0:
    print(A-B*2)
else:
    print(0)