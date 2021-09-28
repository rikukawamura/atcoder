def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
from collections import defaultdict
N = int(input())
S = defaultdict(int)
for _ in range(N):
    x = input()
    S[x] += 1
#pdb.set_trace()

for value in S.values():
    if value != 1:
        print('Yes')
        exit()
print('No')