import pdb

# https://atcoder.jp/contests/abc152/submissions/20625449を参考にした
n = int(input())
p_list = list(map(int, input().split()))

counter = 0
min_num = p_list[0]

for x in p_list:
    if min_num >= x:
        counter += 1
        min_num = x

print(counter)