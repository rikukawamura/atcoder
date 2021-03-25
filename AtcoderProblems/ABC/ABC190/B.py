N, S, D = map(int, input().split())

flag = True
for i in range(N):
    X, Y = map(int, input().split())
    if (X < S) and (Y > D):
        print('Yes')
        flag = False
        break

if flag:
    print('No')