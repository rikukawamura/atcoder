def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
A, B = int_sp()

if 0 < A and  B== 0:
    print('Gold')
elif A == 0 and 0 < B:
    print('Silver')
elif 0 < A and 0 < B :
    print('Alloy')