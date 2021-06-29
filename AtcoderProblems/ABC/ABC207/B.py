def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

A, B, C, D = int_sp()
X = 0
flag = False

for i in range(1, 10**7*1):
    A = A+B
    X = X+C
    if A <= D*X:
        flag = True
        break
if flag:
    print(i)
else:
    print(-1)

