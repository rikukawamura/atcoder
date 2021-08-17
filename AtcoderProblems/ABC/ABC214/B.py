def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
cnt = 0
S, T = int_sp()
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i+j+k <= S and i*j*k <= T:
                cnt += 1
print(cnt)
