'''
TLEになる．https://qiita.com/u2dayo/items/204b73fdb98fa5e4a543を参考にするとうまくいく．
'''

import itertools
import operator
import functools
import pdb

N = int(input())
divs = set()  # 重複を省くために、setを使います

# 数式的にはx <= N ** 0.5 と同じですが、誤差の出ない整数で比較したほうが安全です
x = 1
while x ** 2 <= N:
    if N % x == 0:
        divs.add(x)  # setへの追加はappendではなくaddです
        divs.add(N // x)
    x += 1

ans = list(divs)  # 昇順にしたいので、リストにしてソートします
ans.sort()

for x in ans:
    print(x)
