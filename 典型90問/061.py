def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))


def main():
    from collections import deque
    
    Q = int(input())
    deq = deque()
    for _ in range(Q):
        t, x = int_sp()
        if t == 1:
            deq.append(x)
        elif t == 2:
            deq.appendleft(x)
        else:
            print(deq[-x])




if __name__ == '__main__':
    main()