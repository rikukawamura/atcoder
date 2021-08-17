def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
S = list(input())

index = S.index('1')

if index%2==0:
    print('Takahashi')
else:
    print('Aoki')