def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from math import log

print(log(360, 2))
print(log(10, 2)+(2*log(3,2)))
print(log(5, 2)+(2*log(3,2)+3))
print(log(10, 2)+(3*log(3,2))+3)
print(log(5,2)+(2*log(3,2))+(2*log(4,2)))
print(log(10,2)+log(3,2)+log(4,2))