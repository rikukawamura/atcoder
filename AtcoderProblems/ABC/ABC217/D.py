def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
#import math
import bisect
from collections import deque
import sys
import array
input = sys.stdin.readline
#print(2*(10**5)*math.log(10**9))
L, Q = int_sp()
kireme = array.array('i',[0, L])
for _ in range(Q):
    c, x = int_sp()
    if c == 1:
        kireme.insert(bisect.bisect_left(kireme, x), x)
    elif c == 2:
        index = bisect.bisect_left(kireme, x)
        print(kireme[index] - kireme[index-1])

