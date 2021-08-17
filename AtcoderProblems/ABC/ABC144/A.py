def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
A, B = int_sp()
if 1<= A <= 9 and 1<= B <= 9:
    print(A*B)
else:
    print(-1)