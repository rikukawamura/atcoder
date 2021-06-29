def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

X, K, D = int_sp()
if X < 0:
    X = -X
elif X == 0:
    if K % 2 == 0:
        print(0)
        exit()
    else:
        print(D)
        exit()
cnt = X // D # 正の値で一番最小値の移動回数
minus_cnt = cnt + 1 # 負の中で一番最小値の移動回数

cnt_abs = abs(X-D*cnt) # 正の値の最小値
minus_abs = abs(X-D*minus_cnt) # 負の値の最小値
#pdb.set_trace()

if minus_cnt > K:
    print(X-D*K)
else:
    if (K - cnt) % 2 == 0:
        print(cnt_abs)
    else:
        print(minus_abs)


