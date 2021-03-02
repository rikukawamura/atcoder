import itertools
import pdb

'''
順列問題(回答見た)
itertoolsを覚えた
'''
N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

nums = list(range(1, N))
ans = 0
for index in itertools.permutations(nums):
    #pdb.set_trace()
    index = [0] + list(index)
    ti = 0
    for i in range(N):
        ti += T[index[i]][index[(i + 1) % N]]
    if ti == K:
        ans += 1
print(ans)