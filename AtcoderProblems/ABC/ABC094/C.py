import pdb

N = int(input())
X = list(map(int, input().split()))
X = [[x, i] for i, x in enumerate(X)]
sort_X = sorted(X)


output = [0] * N

for i in range(N):
    tmp = sort_X[:i] + sort_X[i + 1:]
    index = sort_X[i][1]
    output[index] = tmp[(N//2) - 1][0]

for i in output:
    print(i)