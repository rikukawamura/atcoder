x, y = map(int, list(input().split()))

if abs(x-y) < 3:
    print('Yes')
else:
    print('No')