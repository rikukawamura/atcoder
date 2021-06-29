def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

import pdb

N = int(input())

tyokin = 0
for date, x in enumerate(range(1, 10**9), 1):
    #pdb.set_trace()
    tyokin += x
    if tyokin >= N:
        print(date)
        exit()

