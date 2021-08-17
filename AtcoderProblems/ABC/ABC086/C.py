def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
now = 0 # 出発地点の時刻
pre_x, pre_y = 0, 0 # 出発地点
for _ in range(N):
    t, x, y = li_int_sp()
    # 物理的に不可能なパターンとして以下の2点が考えられる．
    # 1. 移動時間内に次の目的地にたどり着けない
    # 2. 偶奇性(パリティ)の関係により，ピッタリ次の目的地にたどり着けない
    if abs(x-pre_x)+abs(y-pre_y) > abs(t-now) or abs(t-now)%2 != (abs(x-pre_x)+abs(y-pre_y))%2:
        print('No')
        exit()
    pre_x, pre_y = x, y
    now = t
print('Yes')
