import pdb
import collections

S = list(input())

flag = False
T = collections.deque()

for s in S:
    if s == 'R':
        flag = not flag
    else:
        if not flag:
            if T and T[-1] == s:
                T.pop()
            else:
                T.append(s)
        else:
            if T and T[0] == s:
                T.popleft()
            else:
                T.appendleft(s)
if flag:
    print(''.join(list(T)[::-1]))
else:
    print(''.join(list(T)))





