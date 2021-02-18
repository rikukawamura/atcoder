import pdb

n = int(input())
xl = [list(map(int, input().split())) for _ in range(n)]
xl = [[i[0]-i[1], i[0]+i[1]] for i in xl]
xl = sorted(xl, key=lambda x: x[1])  #[1]に注目してソート

max_val = -10**10
counter=0
for i in xl:
    if i[0] >= max_val:
        counter+=1
        max_val = i[1]
print(counter)