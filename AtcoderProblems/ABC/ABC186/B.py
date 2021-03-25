'''
H, W = map(int, input().split())

vec = []
tmp_vec = []
total_min = 101

# 全体の最小値を求める
for i in range(H):
    vec = list(map(int, input().split()))
    tmp_vec.append(vec)
    vec_min = min(vec)
    if vec_min < total_min:
        total_min = vec_min

sum = 0
for i in tmp_vec:
    for j in i:
        sum += (j-total_min)
print(sum)
'''

import numpy as np

H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
A = np.array(A)
print(np.sum(A-np.min(A)))



