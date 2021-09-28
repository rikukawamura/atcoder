def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import deque
S = list(input())
deq = deque([])

for s in S:
    if s == '0':
        deq.append(s)
    elif s == '1':
        deq.append(s)
    else:
        if len(deq) > 0:
            deq.pop()
print(''.join(list(deq)))
