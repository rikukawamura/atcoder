import pdb

N, Q = map(int, input().split())
S = input()
AC_count = [0] * (N)

for n in range(0, N-1):
    if S[n:n+2] == 'AC':
        AC_count[n+1] = AC_count[n] + 1
    else:
        AC_count[n+1] = AC_count[n]

for _ in range(Q):
    l, r = map(int, input().split())
    print(AC_count[r-1] - AC_count[l-1])
