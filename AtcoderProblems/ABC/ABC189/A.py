C = list(input())

x = C[0]
y = C[1]
z = C[2]

if x == y and x == z and y == z:
    print('Won')
else:
    print('Lost')