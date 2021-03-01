import pdb


x = list(map(int, input().split()))
for i, j in enumerate(x,1):
    if j == 0:
        print(i)
        exit()