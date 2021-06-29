def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def DeciamlToNine(num):
    "10進数を9進数に変換する"
    nine_number = ""
    while num > 0:
        nine_number += str(num % 9)
        num //= 9
    return int(nine_number[::-1])

def main():
    import pdb

    N, K = int_sp()
    eight_N = N
    if N == 0:
        print(0)
        exit()
    for i in range(K):
        #pdb.set_trace()
        # 8進数を10進数に変換
        ten_N = int('{}'.format(eight_N), 8)
        # 10進数を9進数に変換
        nine_N = DeciamlToNine(ten_N)
        #pdb.set_trace()
        # '8'を'5'に変換（これは8進数とみなす）
        eight_N = str(nine_N).replace('8', '5')

    print(eight_N)



if __name__ == '__main__':
    main()