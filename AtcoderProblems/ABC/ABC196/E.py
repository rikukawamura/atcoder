import pdb


def F(x, A, T):
    for a, t in zip(A, T):
        if t == 1:
            f = x + a
        elif t == 2:
            f = max(x, a)
        elif t == 3:
            f = min(x, a)
        x = f
    print(f)




N = int(input())
tmp = [list(map(int, input().split())) for _ in range(N)]
A, T = list(map(list, (zip(*tmp))))
Q = int(input())
X = list(map(int, input().split()))
for x in X:
    F(x, A, T)
