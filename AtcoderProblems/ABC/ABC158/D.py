def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

import pdb
from collections import deque

S = deque(list(input()))
Q = int(input())

reverse = False
for _ in range(Q):
    #pdb.set_trace()
    x = list(input().split())
    x[0] = int(x[0])
    if len(x) == 3:
        x[1] = int(x[1])
    if x[0] == 1:
        if reverse:
            reverse = False
        else:
            reverse = True
    elif x[0] == 2 and reverse == False:
        if x[1] == 1:
            S.appendleft(x[2])
        elif x[1] == 2:
            S.append(x[2])
    elif x[0] == 2 and reverse == True:
        if x[1] == 1:
            S.append(x[2])
        elif x[1] == 2:
            S.appendleft(x[2])

if reverse:
    print(''.join(list(S)[::-1]))
else:
    print(''.join(S))




