def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮
        return par[x]


def same(x,y):
    return find(x) == find(y)


def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    par[x] = y


import pdb

N,Q = int_sp()
par = [i for i in range(N+1)]
pdb.set_trace()
for i in range(Q):
    p,a,b = map(int,input().split())
    if p == 0:
        unite(a,b)
    else:
        if same(a,b):
            print('Yes')
        else:
            print('No')