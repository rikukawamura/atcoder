import pdb
import collections

S = input()
Q = int(input())
query = [list(map(str, input().split())) for _ in range(Q)]
query_col = collections.Counter(query)
pdb.set_trace()

for i in query:
    #pdb.set_trace()
    if len(i) == 1:
        S = S[::-1]
    elif len(i) == 3:
        if i[1] == '1':
            S = i[2] + S
        elif i[1] == '2':
            S = S + i[2]
print(S)