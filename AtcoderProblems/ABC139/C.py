import pdb

n = int(input())
h = list(map(int, input().split()))

count = 0
tmp = [0]
for i in range(len(h)-1):
    if h[i+1] <= h[i]:
        count += 1
    else:
        count = 0
    tmp.append(count)

print(max(tmp))
