import pdb


S = input()
S = S[::-1]
#print(S)
Q = []

for s in S:
    #print(s)
    if s == '0':
        Q.append('0')
    elif s == '1':
        Q.append('1')
    elif s == '6':
        Q.append('9')
    elif s == '8':
        Q.append('8')
    elif s == '9':
        Q.append('6')
#print(Q)
print(''.join(Q))