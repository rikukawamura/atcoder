def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def main():
    import pdb
    import sys
    import queue

    sys.setrecursionlimit(10000)
    N = int(input())
    G = [[] for i in range(N)]
    for _ in range(N-1):
        A, B = map(int, input().split())
        G[A - 1].append(B - 1)
        G[B - 1].append(A - 1)

    visited = [0]*N
    q = queue.Queue()
    q.put((0, 0))

    def bfs():
        max_id = -1
        max_dis = -1
        while (not q.empty()):
            start, cnt = q.get()
            if visited[start] == 1:
                continue
            else:
                max_id = start
                max_dis = cnt
                visited[start] = 1
                for i in G[start]:
                    q.put((i, cnt+1))
        return max_id, max_dis

    start, cnt = bfs()
    visited = [0]*N
    q.put((start, 0))
    start, cnt = bfs()
    print(cnt+1)


if __name__ == '__main__':
    main()