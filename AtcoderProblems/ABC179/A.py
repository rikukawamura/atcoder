S = input()

if S[-1] != 's':
    output = S + 's'
elif S[-1] == 's':
    output = S + 'es'

print(output)

