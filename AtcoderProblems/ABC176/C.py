N = int(input())
A = list(map(int, input().split()))

height = 0
for i in range(1, N):
    if A[i] < A [i-1]:
        height += A[i-1] - A[i]
        A[i] = A[i-1]
print(height)