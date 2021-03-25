n = int(input())
s, t = map(str, input().split())

output = ''
for a, b in zip(s, t):
    output += a + b
print(output)
