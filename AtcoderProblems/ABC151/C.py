import pdb


n, m = map(int, input().split())
P = [0] * m
S = [0] * m
for i in range(m):
    P[i], S[i] = map(str , input().split())
# 問題によってカウントしたい
WA = [0] * (n+1)
# 全体として何個かがわかればいい
AC = [False] * (n+1)
wa = 0
for i in range(m):
    p = int(P[i])
    # 一度ACになったらその問題は無視
    if AC[p]:
        continue
    # ACになっていない問題の処理
    else:
        # ACになったか判定
        if S[i] == 'AC':
            AC[p] = True
            # ACが通った時のWAのカウントを都度行う必要があるっぽい。違いはわからん
            # 条件でACが出たものに関してWAのカウントをするってなっていた。（条件落としていた。）
            wa += WA[p]
        # ACじゃなかったらWAなので+1していく
        if AC[p] != True:
            WA[p] += 1
# 最後に合計使用するとダメな時がある（条件落としてた）
# wa = sum(WA)（これだとAC出てないものをカウントしちゃう。条件落としてた。）
ac = sum(AC)
print(ac, wa)