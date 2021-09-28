def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
output = []
while N != 0:
    #pdb.set_trace()
    if N%2==0:
        N //= 2
        output.append('B')
    else:
        N -= 1
        output.append('A')
output = output[::-1]
print(''.join(output))

