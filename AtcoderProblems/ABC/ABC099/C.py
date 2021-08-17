def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from bisect import bisect_right

N = int(input())

choises = []
i = 1
j = 1
while 6**i <= 10**6:
    choises.append(6**i)
    i += 1

while 9**j <= 10**6:
    choises.append(9**j)
    j += 1
choises.sort()
choises = [1]+choises

cnt = 0
while N != 0:
    pdb.set_trace()
    x = bisect_right(choises, N)
    N -= choises[x-1]
    print(N, choises[x-1])
    cnt += 1
print(cnt)