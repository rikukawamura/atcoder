import pdb
import itertools

# bit全探索を用いた
n, m = map(int, input().split())
cond = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
human = [list(map(int, input().split())) for _ in range(k)]
indexs = list(itertools.product([0,1], repeat=k))

max_count = 0
for i in indexs:
    count = 0
    tmp = []
    # 人iが皿に置いた組み合わせを作成
    for j, k in zip(human, i):
        tmp.append(j[k])
    #　条件が満たされていればcount+1
    for l in cond:
        if len(set(l) & set(tmp)) == 2:
            count += 1
    # max_countを更新
    if count > max_count:
        max_count = count

print(max_count)