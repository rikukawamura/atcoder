import pdb

N, M = map(int, input().split())

if abs(N-M) > 2:
    print(0)
    exit()
if N == M:
    print((N*M*M) % (10**9+7))
if N > M:
    print((N*M*M) % (10**9+7))
if N < M:
    print((2*M*N*N) % (10**9+7))