import pdb


N, M = map(int, input().split())
root = [[0]*N for _ in range(N)]

for _ in range(M):
    a, b = map(int, input().split())
    # a -> b のrootに可能フラグを立てる(1:移動可能, 0:移動不可)
    root[a-1][b-1] = 1

root_t = list(map(list, (zip(*root))))
if 1 not in root_t[-1]:
    print('IMPOSSIBLE')
    exit()

for i in range(len(root)):
    if root[0][i] == 1 and root_t[-1][i] == 1:
        print('POSSIBLE')
        exit()
print('IMPOSSIBLE')

