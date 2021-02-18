import pdb
from sys import stdin


t = int(input())
output = []
for _ in range(t):
    l, r = map(int, stdin.readline().split())
    count = 0
    for x in range(l, r+1):
        if r-x < l:
            break
        else:
            count += (r-x-l+1)
    output.append(count)
print(*output, sep='\n')



'''
for _ in range(t):
    l, r = map(int, input().split())
    count = 0
    for x in range(l, r+1):
        for y in range(l, x+1):
            c = x - y
            if l <= c <= r:
                count += 1
    print(count)
'''