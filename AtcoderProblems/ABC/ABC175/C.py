import pdb

x, k, d = map(int, input().split())

if abs(x) > 0:
    if k*d > abs(x):
        print(abs(x)%d)
    else:
        print(abs(x)-(k*d))
