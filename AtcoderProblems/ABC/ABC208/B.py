def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from math import factorial

P = int(input())

fact = [factorial(x) for x in range(1, 11)]


total = 0
#pdb.set_trace()
for x in fact[::-1]:
    cnt = 0
    if P//x > 0:
        cnt += P//x
        total += P//x
        P = P-(x*cnt)
print(total)

