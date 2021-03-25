import pdb
import itertools

n, m = map(int, input().split())
total = []
odds = [1+(i*2) for i in range(m)]
evens = [2+(i*2) for i in range(n)]


for i in odds:
    total.append(i)
for i in evens:
    total.append(i)

total = set(total)
#pdb.set_trace()
count = 0

for i in itertools.combinations(total, 2):
    #print(i)
    if sum(i) % 2 == 0:
        count += 1
print(count)