import pdb

n, k = map(int, input().split())

a = []
for i in range(k):
    d = int(input())
    for j in input().split():
        if j not in a:
            a.append(j)

print(n-len(a))