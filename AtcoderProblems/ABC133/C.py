import pdb

L, R = map(int, input().split())

opt = 2019
flag = False
for i in range(L, R+1):
    for j in range(i+1, R+1):
        x = (i*j) % 2019
        if x < opt:
            opt = x
        if opt == 0:
            flag = True
            break
    if flag:
        break
print(opt)