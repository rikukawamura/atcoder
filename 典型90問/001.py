def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def main():
    import pdb

    N, L = int_sp()
    K = int(input())
    A = li_int_sp()
    dif = []
    for i in range(1, N):
        dif.append(A[i]-A[i-1])
    dif.append(L-A[-1])
    dif.insert(0, A[0])

    def cnt_count(x):
        length = 0
        cnt = 0
        for i in dif:
            length += i
            if length >= x:
                cnt += 1
                length = 0
        return cnt

    left = 0
    right = L
    while right - left > 1:
        #探索範囲の動き方を確認できるよ．
        print(right, left)
        mid = (left + right) // 2
        # cntがK+1以上なら最も短いものの長さを長くできる可能性がある．
        if cnt_count(mid) >= K+1:
            left = mid
        else:
            right = mid
    print(left)

if __name__ == '__main__':
    main()