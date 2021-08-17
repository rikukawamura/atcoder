import pdb

N = int(input())
X = list(map(int, input().split()))
X_sort = sorted(X)
X = [[i, x] for i, x in enumerate(X)]
mid = N//2

#pdb.set_trace()
total = [0] * N
for i, x in X:
    if x < X_sort[mid]:
        total[i] = X_sort[mid]
    else:
        total[i] = X_sort[mid-1]

for i in total:
    print(i)
