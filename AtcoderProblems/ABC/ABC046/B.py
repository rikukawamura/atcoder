def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N, K = int_sp()
if N == 1:
    print(K)
else:
    print(K * ((K-1)**(N-1)))