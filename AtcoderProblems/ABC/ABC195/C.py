import pdb

N = int(input())
x = (len(str(N))-1) // 3

count = 0
while x != 0:
    #pdb.set_trace()
    count += (N - 10**(3*x) + 1) * x
    N = 10**(3*x) - 1
    x -= 1
print(count)