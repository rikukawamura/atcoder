from math import factorial
import pdb


# ----------------------------------------------------------------------------------------------------------

def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# リストのリストの単一の要素を抽出 (リストのset)
# [[1, 1], [0, 1], [0, 1], [0, 0], [1, 0], [1, 1], [1, 1]] -> [[1, 1], [0, 1], [0, 0], [1, 0]]
def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


# ----------------------------------------------------------------------------------------------------------
# 配列の操作でなんとかなる．

def main():
    from collections import defaultdict
    odd = defaultdict(int)
    even = defaultdict(int)

    N = int(input())
    V = li_int_sp()

    for i, v in enumerate(V):
        if i % 2 == 0:
            even[v] += 1
        else:
            odd[v] += 1

    pdb.set_trace()
    if len(odd) == len(even) == 1 and even.keys() == odd.keys():
        print(N // 2)
        exit()

    odd = sorted(odd.items(), reverse=False, key=lambda x: x[1])
    even = sorted(even.items(), reverse=False, key=lambda x: x[1])
    if len(odd) == 1 and len(even) > 1:
        print((N // 2 - odd[0][1]) + (N // 2 - even[1][1]))
    elif len(odd) > 1 and len(even) == 1:
        print((N // 2 - odd[1][1]) + (N // 2 - even[0][1]))
    else:
        min_val = float('INF')
        if len(odd) > 1 and len(even) > 1:
            for i in range(2):
                for j in range(2):
                    if odd[i][1] != even[j][i]:
                        min_val = min(min_val, (N//2-odd[i][1])+(N//2-even[j][1]))
        print(min_val)
        



if __name__ == '__main__':
    main()