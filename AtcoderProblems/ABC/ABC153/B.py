import itertools

h, n = map(int, input().split())
a = list(map(int, input().split()))
acc_a = list(itertools.accumulate(a))

if h <= acc_a[-1]:
    print('Yes')
else:
    print('No')