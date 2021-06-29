import pdb

S1 = input()
S2 = input()
S3 = input()

S1_len = len(S1)
S2_len = len(S2)
S3_len = len(S3)

if S1 == S3 or S2 == S3:
    print('UNSOLVABLE')
    exit()

'''
if S1_len <= 1:
    S1_range = range(1, 10)
elif S1_len <= 2:
    S1_range = range(10, 100)
elif S1_len <= 3:
    S1_range = range(100, 1000)
elif S1_len <= 4:
    S1_range = range(1000, 10000)
elif S1_len <= 5:
    S1_range = range(10000, 100000)
elif S1_len <= 6:
    S1_range = range(100000, 1000000)
elif S1_len <= 7:
    S1_range = range(1000000, 10000000)
elif S1_len <= 8:
    S1_range = range(10000000, 100000000)
elif S1_len <= 9:
    S1_range = range(100000000, 1000000000)
elif S1_len <= 10:
    S1_range = range(10000000, 10000000000)
'''