def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

import pdb
import math
import queue
import heapq
Q = int(input())
A = queue.Queue()
B = []
heapq.heapify(B)
push_list = [False]*10
sort_flag = False
i = 0
for _ in range(Q):
    pdb.set_trace()
    X = li_int_sp()
    if X[0] == 1:
        A.put((X[1], i))
        heapq.heappush(B, (X[1], i))
        i+=1
    elif X[0] == 2:
        if sort_flag:
            while True:
                x = heapq.heappop(B)
                if push_list[x[1]] == True:
                    continue
                else:
                    push_list[x[1]] = True
                    print(x[0])
                    break
        else:
            while True:
                x = A.get()
                if push_list[x[1]] == True:
                    continue
                else:
                    push_list[x[1]] = True
                    print(x[0])
                    break
    elif X[0] == 3:
        sort_flag = not sort_flag

