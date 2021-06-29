def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

from math import floor

N = int(input())
x = floor(1.08*N)
if x < 206:
    print('Yay!')
elif x == 206:
    print('so-so')
else:
    print(':(')