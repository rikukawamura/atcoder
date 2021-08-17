def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
N = int(input())
if 1 <= N <= 125:
    print(4)
elif 126 <= N <= 211:
    print(6)
else:
    print(8)