'''
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
output = 0
for j in A:
    start = j[0]
    end = j[1]
    output += sum(range(start, end+1))

print(output)
'''