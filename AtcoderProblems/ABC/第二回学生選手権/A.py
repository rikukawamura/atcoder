import pdb

X, Y, Z = map(int, input().split())

takahashi = Y/X
#pdb.set_trace()

for i in reversed(range(10**6+1)):
    if i/Z < takahashi:
        print(i)
        exit()