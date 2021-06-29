def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def main():
    import pdb
    from collections import deque


    N = int(input())
    for bit in range(2**N-1):
        count = 0
        x = deque()
        for i in range(N)[::-1]:
            if 1 & (bit >> i):
                count -= 1
                x.append(')')
                if count < 0:
                    break
            else:
                count += 1
                x.append('(')
        if count == 0:
            print(''.join(x))



if __name__ == '__main__':
    main()