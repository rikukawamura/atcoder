import itertools
import copy
import pdb


s = list(input())
n = len(s)
output = 0

for i in range(2**(n-1)):
    l = s.copy()
    for j in range(n-1):
        if bin(i >> j)[-1] == '1':
            l.insert(n-j-1, '+')
    y = (''.join(l)).split('+')
    output += sum(map(int, y))
print(output)

