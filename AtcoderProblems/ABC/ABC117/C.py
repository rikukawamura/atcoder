import pdb

N, M = map(int, input().split())
X = sorted(list(map(int, input().split())))
x_diff = [0] * (M-1)

# 未解決問題(コメント外すとAC)
'''
if N >= M:
    print(0)
    exit()
'''

for i in range(0, M-1):
    x_diff[i] = X[i+1] - X[i]

x_diff = sorted(x_diff)
pdb.set_trace()
print(sum(x_diff[:M-N]))


