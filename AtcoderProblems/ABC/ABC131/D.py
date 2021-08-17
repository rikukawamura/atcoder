def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))


import pdb

N = int(input())
lists = [li_int_sp() for _ in range(N)]
lists = sorted(lists, key=lambda x:x[1])

total_time = 0
for time, dline in lists:
    total_time += time
    if total_time > dline:
        print('No')
        exit()
print('Yes')
