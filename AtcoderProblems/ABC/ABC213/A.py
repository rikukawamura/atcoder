def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
A, B = int_sp()
C = 0
while True:
    if A ^ C == B:
        print(C)
        exit()
    else:
        C += 1
