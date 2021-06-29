# 単純な問題文の読み間違い
# 8色のどれかに自由に色を変えれると考えていたが，どうやら何色でも変化できるらしい．
# 今まで解いた問題の中で1番のクソ問題だった．

import pdb

N = int(input())
A = list(map(int, input().split()))

colors = {'灰':False, '茶':False, '緑':False, '水':False, '青':False, '黄':False, '橙':False, '赤':False}

overspec = 0
for a in A:
    if 1 <= a <= 399:
        colors['灰'] = True
    elif 400 <= a <= 799:
        colors['茶'] = True
    elif 800 <= a <= 1199:
        colors['緑'] = True
    elif 1200 <= a <= 1599:
        colors['水'] = True
    elif 1600 <= a <= 1999:
        colors['青'] = True
    elif 2000 <= a <= 2399:
        colors['黄'] = True
    elif 2400 <= a <= 2799:
        colors['橙'] = True
    elif 2800 <= a <= 3199:
        colors['赤'] = True
    else:
        overspec += 1

x = [key for key, val in zip(colors.keys(), colors.values()) if val == True]
len_x = len(x)

if len_x == 0:
    min_val = 1
    max_val = overspec
    print(min_val, max_val)
    exit()


min_val = len_x
max_val = len_x + overspec

print(min_val, max_val)
