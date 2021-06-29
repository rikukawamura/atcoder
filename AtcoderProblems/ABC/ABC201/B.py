def int_split():
    return map(int, input().split())

def list_int_split():
    return list(map(int, input().split()))

import pdb
import itertools


st = []
N = int(input())

for _ in range(N):
    s, t = input().split()
    t = int(t)
    st.append([s,t])

#print(st)

sorted_st = sorted(st, reverse=True, key=lambda x: x[1])
print(sorted_st[1][0])