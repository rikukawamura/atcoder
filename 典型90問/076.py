def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from itertools import accumulate

N = int(input())
A = li_int_sp()
double_A = A+A
x = sum(A)/10
acc_A = list(accumulate(double_A))

r = 0
for l in range(N):
    while r < len(acc_A):
        tmp = acc_A[r]-acc_A[l]
        if tmp == x:
            print('Yes')
            exit()
        elif tmp > x:
            break
        r += 1

    if l == r:
        r += 1
print('No')

