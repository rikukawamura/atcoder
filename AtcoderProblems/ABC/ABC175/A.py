import itertools
import pdb

s = list(input())
s_list = []
for key, value in itertools.groupby(s):
    if key == 'R':
        s_list.append(len(list(value)))

if s_list == []:
    print(0)
else:
    print(max(s_list))

