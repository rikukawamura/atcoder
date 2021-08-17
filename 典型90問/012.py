def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y
'''
def unite(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    if x < y:
        x, y = y, x
    par[x] = y
'''

import pdb

h, w = map(int,input().split())
q = int(input())

# H行W列を一次元に置き直す．
# インデックスは0から始まるため，+1してあげる．
par = [i for i in range(h * w + 1)]
# gridでout of rangeにならないように，(w+2)*(h+2)マス用意．
grid = [[False] * (w+2) for _ in range(h+2)]
# 4方向に対する変化量
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
pdb.set_trace()
for i in range(q):
    a = list(map(int,input().split()))
    if a[0] == 1:
        grid[a[1]][a[2]] = True
        for dy, dx in d:
            if grid[a[1] + dy][a[2] + dx] == True: # 周囲４方向が塗られていれば、連結させる
                unite((a[1] + dy - 1) * w + (a[2] + dx), (a[1] - 1) * w + a[2])
    elif a[0] == 2:
        # 連結している & 2つのマスが赤色になっていればYes
        # 1マスも赤色で塗られていない場合があるため，gridが必要である．
        if same((a[1] - 1) * w + a[2], (a[3] - 1) * w + a[4]) and grid[a[1]][a[2]] and grid[a[3]][a[4]]:
            print("Yes")
        else:
            print("No")
