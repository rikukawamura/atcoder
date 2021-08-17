def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N, X = int_sp()
A = li_int_sp()
for i, a in enumerate(A, 1):
    if i%2 == 1:
        X-=a
    else:
        X-=(a-1)

if X >= 0:
    print('Yes')
else:
    print('No')
