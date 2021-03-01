import pdb


n = int(input())
#apx = [list(map(int, input().split())) for _ in range(n)]
nedan = []
#pdb.set_trace()
for _ in range(n):
    a, p, x = map(int, input().split())
    x = x - (a)
    if x > 0:
        nedan.append(p)
#pdb.set_trace()
if nedan != []:
    print(min(nedan))
else:
    print(-1)

