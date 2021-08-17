def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())

for i in range(1, 10):
    for j in range(1, 10):
        if i*j == N:
            print('Yes')
            exit()

print('No')
