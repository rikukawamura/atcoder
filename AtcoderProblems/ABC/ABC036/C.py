def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def compress(arr:list) -> dict:
    pdb.set_trace()
    *XS, = set(arr)
    XS.sort()
    return {e: i for i, e in enumerate(XS)}

import pdb
N = int(input())
A = []
for _ in range(N):
    x = int(input())
    A.append(x)
dict = compress(A)
#pdb.set_trace()

for a in A:
    print(dict[a])