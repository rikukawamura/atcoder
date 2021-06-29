import pdb
import sys

input = sys.stdin.readline
N = int(input())
S = list(input().strip())
Q = int(input())

reverse = False

for _ in range(Q):
    t, a, b = map(int, input().split())
    if reverse:
        if a <= N:
            a = a + N
        else:
            a = a - N

        if b <= N:
            b = b + N
        else:
            b = b - N

    if t == 1:
        S[a-1], S[b-1] = S[b-1], S[a-1]
    elif t == 2:
        reverse = not reverse

if reverse:
    print(''.join(S[N:]+S[:N]))
else:
    print(''.join(S))




