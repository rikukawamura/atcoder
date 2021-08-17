def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
A = li_int_sp()
A_mod = []
for i in A:
    A_mod.append(i%2)
pdb.set_trace()

