import pdb

H = int(input())

x = 1
count = 1
while H != 1:
    H //= 2
    count += 2**x
    x += 1

print(count)
