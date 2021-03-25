import pdb
import itertools as iter
import collections as col

n = int(input())
a = [int(input()) for _ in range(n)]
col_a = col.Counter(sorted(a, reverse=True))
group_dict = [] # 各要素の個数（ソートしている）
for key, group in zip(col_a.keys(), col_a.values()):
    group_dict.append([key, group])
# 最大値を取得
max_val = group_dict[0][0]

if len(group_dict) == 1:
    for i in a:
        print(max_val)
else:
    for i in a:
        if i == max_val and group_dict[0][1] == 1:
            print(group_dict[1][0])
        elif i == max_val and group_dict[0][1] != 1:
            print(group_dict[0][0])
        else:
            print(max_val)

