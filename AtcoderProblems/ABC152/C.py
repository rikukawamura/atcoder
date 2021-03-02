import pdb

n = int(input())
p = list(map(int, input().split()))

count = 0
for i in range(n):
    if p[i] <= min(p[:i+1]):
        count += 1
print(count)