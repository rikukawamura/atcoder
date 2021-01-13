N = int(input())
d = []
for i in range(N):
    d.append(int(input()))
d = sorted(d, reverse=True)

count = 1
idx = d[0]
for j in d[1:]:
    if j < idx:
        idx = j
        count += 1

print(count)

