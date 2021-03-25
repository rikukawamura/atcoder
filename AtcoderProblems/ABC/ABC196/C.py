import pdb
import itertools

N = int(input())
len_N = len(str(N))//2
tmp = [9, 10*9, 10**2*9, 10**3*9, 10**4*9, 10**5*9]
num_acc = list(itertools.accumulate(tmp))
#pdb.set_trace()
# Nの長さが1の場合
if len_N == 0:
    print(0)
# Nの長さが2,3の場合
elif len_N == 1:
    count = 0
    zoro = 11
    while zoro <= N and zoro <= 99:
        count += 1
        zoro += 11
    print(count)
# Nの長さが4,5の場合
elif len_N == 2:
    count = num_acc[0]
    zoro = 1010
    while zoro <= N and zoro <= 9999:
        count += 1
        zoro += 101
    print(count)
# Nの長さが6,7
elif len_N == 3:
    count = num_acc[1]
    zoro = 100100
    while zoro <= N and zoro <= 999999:
        count += 1
        zoro += 1001
    print(count)
# Nの長さが8,9
elif len_N == 4:
    count = num_acc[2]
    zoro = 10001000
    while zoro <= N and zoro <= 99999999:
        count += 1
        zoro += 10001
    print(count)
# Nの長さが10,11
elif len_N == 5:
    count = num_acc[3]
    zoro = 1000010000
    while zoro <= N and zoro <= 9999999999:
        count += 1
        zoro += 100001
    print(count)
# Nの長さが12
elif len_N == 6:
    count = num_acc[4]
    zoro = 100000100000
    while zoro <= N and zoro <= 999999999999:
        count += 1
        zoro += 1000001
    print(count)

