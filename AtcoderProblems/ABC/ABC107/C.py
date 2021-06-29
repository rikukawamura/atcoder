import pdb

N, K = map(int, input().split())
X = list(map(int, input().split()))

min_val = float('INF')
#total = []
for i in range(N-K+1):
    tmp_l = X[i]
    tmp_r = X[K-1+i]
    x = abs(tmp_l) + abs(tmp_r-tmp_l)
    y = abs(tmp_r) + abs(tmp_r-tmp_l)
    #total.append(x)
    #total.append(y)
    min_val = min(min_val, x)
    min_val = min(min_val, y)
print(min_val)