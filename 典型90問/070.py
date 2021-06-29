def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


import pdb

N = int(input())
X, Y = list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))
#pdb.set_trace()

X = sorted(X)
Y = sorted(Y)
dis_x = 0
dis_y = 0
mid = N//2
if N%2==1:
    mid_x = X[mid]
    mid_y = Y[mid]
    for x, y in zip(X, Y):
        dis_x += abs(x-mid_x)
        dis_y += abs(y-mid_y)
else:
    mid_x = (X[mid-1]+X[mid])//2
    mid_y = (Y[mid-1]+Y[mid])//2
    for x, y in zip(X, Y):
        dis_x += abs(x-mid_x)
        dis_y += abs(y-mid_y)
print(dis_x+dis_y)

