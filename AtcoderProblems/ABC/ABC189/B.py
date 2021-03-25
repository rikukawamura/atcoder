import pdb

N, X = map(int, input().split())
X = 100 * X

sum_alc = 0
flag = True
for n in range(1, N+1):
    V, P = map(int, input().split())
    sum_alc += (V * P)
    if sum_alc > X:
        print(n)
        flag = False
        break

if flag:
    print(-1)