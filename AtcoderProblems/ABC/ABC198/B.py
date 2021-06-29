import pdb

N = input()
M = N.strip('0')

if M == M[::-1]:
    print('Yes')
else:
    print('No')