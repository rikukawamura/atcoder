def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

"""nを素因数分解"""
"""2以上の整数n => [[素因数, 指数], ...]の2次元リスト"""
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


import pdb
N = int(input())
divs = factorization(N)
output = []
for i, j in divs:
    pdb.set_trace()
    tmp = []
    ind = 2
    if i >= 2:
        tmp.append('AA')
    elif i == 1:
        tmp.append('A')
    while 2 ** ind <= i:
        ind += 1
    if ind-2 != 0:
        tmp += ['B' * (ind - 2)]
    #pdb.set_trace()
    mods = i - 2**(ind - 1)
    if mods != 0:
        tmp += ['A' * mods]
    tmp = tmp*j
    output += tmp

print(''.join(output))
