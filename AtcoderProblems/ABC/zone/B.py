import pdb


N, D, H = map(int, input().split())
dh = [list(map(int, input().split())) for _ in range(N)]

#katamuki = -float('INF')
katamuki = []
for i, d in enumerate(dh):
    tmp = (d[1]-H)/(d[0]-D)
    katamuki.append(tmp)
#pdb.set_trace()
min_katamuki = min(katamuki)
min_index = katamuki.index(min_katamuki)

#ten = dh[index]
#pdb.set_trace()
y = min_katamuki * (0-dh[min_index][0]) + dh[min_index][1]
if y < 0:
    print(0.0)
else:
    print(y)

