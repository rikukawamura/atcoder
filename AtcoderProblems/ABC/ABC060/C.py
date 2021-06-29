import pdb

N, T = map(int, input().split())
t = list(map(int, input().split()))

dif = []
for i in range(N-1):
    dif.append(t[i+1]-t[i])

count = 0
for j in dif:
    if j < T:
        count += j
    else:
        count += T
count += T
print(count)
