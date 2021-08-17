def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
N = int(input())
A = li_int_sp()

B = []
for i, a in enumerate(A, 1):
    B.append(a-i)
B = sorted(B)
if N%2==1:
    mid = B[N//2]
else:
    mid = (B[N//2]+B[N//2-1])//2
#pdb.set_trace()
output = 0
for i in B:
    output += abs(i-mid)
print(output)