import pdb


N = int(input())
X = [list(map(int, input().split())) for _ in range(N)]
Xt = list(map(list, (zip(*X))))
#pdb.set_trace()

total = []
for i in Xt:
    total.append(max(i))
print(min(total))