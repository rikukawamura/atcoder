import pdb

N, K = map(int, input().split())
for _ in range(K):
    if N%200 == 0:
        N = N // 200
    else:
        N = str(N) + str(200)
        N = int(N)

print(N)