import itertools
import pdb

'''
S = list(map(int, list(input())))
flag = True

if len(S) < 3:
    for num in range(1, len(S)+1):
        for i in itertools.permutations(S, num):
            if int(''.join(map(str, i[-3:]))) % 8 == 0:
                print('Yes')
                flag = False
                break
        if not flag:
            break
else:
    for i in itertools.permutations(S, 3):
        if int(''.join(map(str, i[-3:]))) % 8 == 0:
            print('Yes')
            flag = False
            break

if flag:
    print('No')
'''

from collections import Counter
n = input()
if len(n) <= 2:
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()
cnt = Counter(n)
pdb.set_trace()
for i in range(112, 1000, 8):
    if not Counter(str(i)) - cnt:
        print("Yes")
        exit()
print("No")