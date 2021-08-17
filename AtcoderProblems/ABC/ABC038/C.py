def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict

N = int(input())
A = li_int_sp()

l, r, ans = 0, 1, 0
while l < N:
    if l == N-1:
        ans+=1
        break
    while True:
        if r >= N:
            break
        if A[r-1] >= A[r]:
            break
        r+=1
    ans += r-l
    l += 1

    if l == r:
        r += 1
print(ans)
