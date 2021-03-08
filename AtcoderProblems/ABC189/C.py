import pdb
import itertools

#　これ難しかった（一見難しそうに見えても全探索でなんとかなる）
# 計算量がきついと思ったが，サンプルテストが制限ギリギリをせめていないらしい
# https://qiita.com/u2dayo/items/edd462bf0d8b2f2df55f#commentsを参考
N = int(input())
A = [*map(int, input().split())]

ans = 0
# lを固定
for l in range(N):
    m = 10 ** 6  # 適当な10 ** 5より大きい数で初期化
    # rを固定
    for r in range(l, N):
        d = r - l + 1  # 区間の幅
        m = min(m, A[r])  # 区間の最小を更新
        score = m * d  # 食べたみかん
        ans = max(ans, score)

print(ans)