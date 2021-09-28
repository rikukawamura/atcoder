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
    s = input()
    S[s] += 1

sort_s = sorted(S.items(), key=lambda x:x[1], reverse=True)
#pdb.set_trace()
print(sort_s[0][0])