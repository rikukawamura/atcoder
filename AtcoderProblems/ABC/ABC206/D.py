def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

import pdb


N = int(input())
A = li_int_sp()

if N == 1:
    print(0)
else:
    maps = [[0]*N for _ in range(N)]
    if N % 2 == 1:
        nor = A[:N//2]
        mid = [N//2+1]
        rev = A[N//2+1:][::-1]
    else:
        nor = A[:N//2]
        rev = A[N//2:][::-1]
    #pdb.set_trace()

for n, r in zip(nor, rev):
    if n != r:
        maps[n-1][r-1] += 1
        maps[r-1][n-1] += 1

print(0)



