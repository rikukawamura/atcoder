def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
S = input()

r, ans, maru, batu = 0, 0, 0, 0
for l in range(N):
    while r < N and (maru==0 or batu==0) :
        if S[r] == 'o':
            maru+=1
        elif S[r]== 'x':
            batu+=1
        r+=1
    if maru!=0 and batu!=0: # r<Nの条件でも抜けてくるので，この条件が必要．
        ans+=N-(r-1)
    if l == r:
        r+=1
    else:
        if S[l] == 'o':
            maru-=1
        elif S[l] == 'x':
            batu -= 1
print(ans)
