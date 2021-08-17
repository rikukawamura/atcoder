def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import accumulate

X = int(input())
acc = list(accumulate(range(1, 10**6)))

if X == 1:
    print(1)
    exit()

for next, x in enumerate(acc, 2):
    print(next+x)
    if next+x >= X:
        break

print(next)


