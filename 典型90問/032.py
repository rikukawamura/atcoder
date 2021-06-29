def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def main():
    import pdb
    from itertools import permutations


    N = int(input())
    A = [li_int_sp() for _ in range(N)]
    M = int(input())
    kenaku = [[0] * N for _ in range(N)]
    if M != 0:
        X, Y = list(map(list, (zip(*[li_int_sp() for _ in range(M)]))))
        for x, y in zip(X, Y):
            kenaku[x-1][y-1] = 1
            kenaku[y-1][x-1] = 1


    min_time = []
    for i in permutations(range(N)):
        temp = 0
        flag = True
        #pdb.set_trace()
        before_runner = i[0]
        temp += A[i[0]][0]
        for kukan, j in enumerate(i[1:], 1):
            if kenaku[before_runner][j] == 1:
                flag = False
            else:
                temp += A[j][kukan]
                before_runner = j
        if flag:
            min_time.append(temp)
    if min_time != []:
        print(min(min_time))
    else:
        print(-1)




if __name__ == '__main__':
    main()