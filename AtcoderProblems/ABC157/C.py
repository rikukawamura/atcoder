import pdb

n, m = map(int, input().split())
output = [0] * n

condition = []
for _ in range(m):
    x = list(map(int, input().split()))
    if x in condition:
        continue
    else:
        condition.append(x)

for cond in condition:
    if cond[0] == 1 and cond[1] == 0:
        print(-1)
        exit()
    if (output[(cond[0]-1)] != 0):
        print(-1)
        exit()
    else:
        output[(cond[0]-1)] = cond[1]
if output[0] == 0:
    output[0] = 1
print(''.join(list(map(str, output))))

