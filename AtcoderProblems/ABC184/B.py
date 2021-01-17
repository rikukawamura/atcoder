N, X = map(int, input().split())
S = list(input())

for i in S:
    if i == 'o':
        X += 1
    if X != 0 and i == 'x':
        X -= 1

print(X)