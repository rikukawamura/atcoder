'''時間かかった'''
N, M, T = list(map(int, input().split()))
max_N = N
start = 0

for i in range(M):
    if N > 0:
        A, B = list(map(int, input().split()))
        N -= (A - start) // 1
        if N > 0:
            N += (B - A) // 1
            if N > max_N:
                N = max_N
            start = B
        else:
            break
    else:
        break


if N > 0:
    N -= (T - B) // 1

if N <= 0:
    print('No')
else:
    print('Yes')



