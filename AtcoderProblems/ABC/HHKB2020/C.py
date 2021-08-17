def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb
import bisect

N = int(input())
P = li_int_sp()

deta =[False]*(2*(10**5)+2) # 既出の数値を記録
min_val = 0 # 出力する値

for p in P:
    deta[p] = True
    # 現在の最小値がTrueになるまでは，現在の最小値を出力する．
    # しかし，出た値は記録していく．
    # 現在の最小値がTrueとなると，detaの中を降順に見ていき，Falseとなっている値が次の最小値となる．
    while deta[min_val]:
        min_val += 1
    print(min_val)



