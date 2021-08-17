def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

X, Y, A, B = int_sp()
min_zimu = min(A, B)

if min_zimu == 1:
    print(Y-X-1)
    exit()
if A >= Y and B>=Y:
    print(0)
    exit()

i = 1
keikenti = 0
while True:
    nxt = X*A
    if nxt-X < B:
        keikenti += 1
        X = nxt
    else:
        break

print((Y-X-1)//B+keikenti)