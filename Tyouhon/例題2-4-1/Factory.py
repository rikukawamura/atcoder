import heapq
import pdb

N, K = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
ab = list(map(list, (zip(*ab))))
a = ab[0]
b = ab[1]

hp = []
heapq.heapify(hp)
for i, a in enumerate(a):
    heapq.heappush(hp, [a, i])

total_time = 0
for _ in range(K):
    time, index = heapq.heappop(hp)
    total_time += time
    heapq.heappush(hp, [time+b[index], index])
print(total_time)