N, X, T = map(int, input().split())

if N % X != 0:
    each = N // X + 1
else:
    each = N //X
total_time = T * each
print(total_time)