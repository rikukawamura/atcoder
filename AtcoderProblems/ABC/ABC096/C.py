import pdb

H, W = map(int, input().split())
dxdy = ((-1,0), (1,0), (0,-1), (0,1))

campus = []
for i in range(H):
    campus.append(list(input()))

for y in range(H):
    for x in range(W):
        if campus[y][x] == '#':
            flag = False
            for dy, dx in dxdy:
                if (0 <= y+dy < H) and (0 <= x+dx < W):
                    if campus[y+dy][x+dx] == '#':
                        flag = True

            if flag == False:
                print('No')
                exit()
print('Yes')

