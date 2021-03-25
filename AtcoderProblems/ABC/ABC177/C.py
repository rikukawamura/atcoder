import itertools


N = int(input())
A = list(map(int, input().split()))

total = 0
cusum = list(itertools.accumulate(A))
for i, a in enumerate(A[:-1]):
    total += (A[i] * (cusum[-1] - cusum[i]))
print(total % (10**9+7))
