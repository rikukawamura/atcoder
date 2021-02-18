import itertools
import copy
import pdb


s = list(input())
n = len(s)
output = 0
for i in range(2**(n-1)):
    l = s.copy()
    for j in range(n-1):
        if bin(i >> j)[-1] == '0':
            l.insert(n-j-1, '-')
        elif bin(i >> j)[-1] == '1':
            l.insert(n-j-1, '+')
    output = ''.join(l)
    if output[1] == '-':
        y = int(output[0]) - int(output[2])
    elif output[1] == '+':
        y = int(output[0]) + int(output[2])
    if output[3] == '-':
        y -= int(output[4])
    elif output[3] == '+':
        y += int(output[4])
    if output[5] == '-':
        y -= int(output[6])
    elif output[5] == '+':
        y += int(output[6])
    if y == 7:
        print(output+'=7')
        exit()

