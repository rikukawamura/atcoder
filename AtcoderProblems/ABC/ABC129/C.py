import pdb

N, M = map(int, input().split())
A = [int(input()) for _ in range(M)]
X = [x for x in range(0, N+1) if x not in A]

output = 1
for i in X:
    tmp = 0
    if i == N:
        break
    else:
        if i+1 in X:
            tmp += 1
        if i+2 in X:
            tmp += 1
    output *= tmp

print(output % ((10**9)+7))