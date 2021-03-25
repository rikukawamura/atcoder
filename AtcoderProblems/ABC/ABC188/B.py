N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

sum = 0
for a, b in zip(A, B):
    sum += a*b

if sum == 0:
    print('Yes')
else:
    print('No')