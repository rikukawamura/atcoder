import pdb

uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

N = int(input())
S = list(map(str, input()))

new_string = []
for s in S:
    x = uppercase.index(s)
    new_string.append(uppercase[(x+N)%26])
print(''.join(new_string))

