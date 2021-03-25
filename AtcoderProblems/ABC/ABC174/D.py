import pdb

N = int(input())
C = list(input())
red = [i for i, x in enumerate(C) if x == 'R'][::-1]
white = [i for i, x in enumerate(C) if x == 'W']
l_red = len(red)
l_white = len(white)

i = 0
count = 0
if l_red >= l_white:
    for r, w in zip(red, white):
        if w < r:
            white[i] = r
            red[i] = w
            count += 1
        i += 1
elif l_red < l_white:
    for r, w in zip(red, white):
        if w < r:
            white[i] = r
            red[i] = w
            count += 1
        i += 1

print(count)

