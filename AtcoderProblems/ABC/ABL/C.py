def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


# おまじない
import sys
import pdb


sys.setrecursionlimit(10000)
# 入力の読み込み
N,M=map(int,input().split())
G=[[] for i in range(N)]
# G[i] は都市iから道路で直接繋がっている都市のリスト
for i in range(M):
  A,B=map(int,input().split())
  G[A-1].append(B-1)
  G[B-1].append(A-1)

print(N-1-M)

