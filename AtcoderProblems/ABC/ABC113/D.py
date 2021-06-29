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
    # 各県に[出てきた順, 市の生まれ年]を格納
    #X = []
    N, M = int_sp()
    X = [[] for i in range(N)]
    for i in range(M):
        P, Y = int_sp()
        X[P-1].append([i, Y])
    pdb.set_trace()

    # [出てきた順,　市の生まれ年,　県ごとに市の生まれ年をsortした順番]を格納
    Y = [[] for i in range(N)]
    for ind1, i in enumerate(X):
        for ind2, j in enumerate(sorted(i, reverse=False, key=lambda x: x[1])):
            Y[ind1].append([j[0], j[1], ind2])
    
    pdb.set_trace()
    出てきた順のindexにP_i + x を格納
    output = [[] for i in range(M)]
    for ind, y in enumerate(Y):
        for i in y:
            output[i[0]].append(str(ind+1).zfill(6)+str(i[2]+1).zfill(6))

    for i in output:
        print(*i)




if __name__ == '__main__':
    main()