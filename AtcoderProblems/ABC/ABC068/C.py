import pdb


N, M = map(int, input().split())
cnt = [0]*N
start_to_x = []
x_to_goal = []
for _ in range(M):
    a, b = map(int, input().split())
    if a == 1:
        start_to_x.append(b)
    elif b == 1:
        start_to_xj.append(a)
    elif a == N:
        x_to_goal.append(b)
    elif b == N:
        x_to_goal.append(a)

start_to_x = set(start_to_x)
x_to_goal = set(x_to_goal)

if len(start_to_x & x_to_goal) != 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')


