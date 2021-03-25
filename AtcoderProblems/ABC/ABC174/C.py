import sys
import pdb
flag = True
K = int(input())

j = 0
for i in range(0, 10**6+1):
    j = j * 10 + 7
    if j % K == 0:
        print(i+1)
        flag = False
        break

if flag:
    print(-1)