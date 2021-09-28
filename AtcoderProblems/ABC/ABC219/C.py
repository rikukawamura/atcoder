def int_sp():
    return map(int, input().split())


def li_int_sp():
    return list(map(int, input().split()))

def trans_li_int_sp():
    return list(map(list, (zip(*[li_int_sp() for _ in range(N)]))))

def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

import pdb
import math
X = list(input())
#dict = {'a':X[0], 'b':X[1], 'c':X[2], 'd':X[3],'e':X[4],'f':X[5],'g':X[6],'h':X[7],'i':X[8],'j':X[9],'k':X[10],'l':X[11],'m':X[12],'n':X[13],'o':X[14],'p':X[15],'q':X[16],'r':X[17],'s':X[18],'t':X[19],'u':X[20],'v':X[21],'w':X[22],'x':X[23],'y':X[24],'z':X[25]}
dict = {X[0]:'a', X[1]:'b', X[2]:'c', X[3]:'d',X[4]:'e',X[5]:'f',X[6]:'g',X[7]:'h',X[8]:'i',X[9]:'j',X[10]:'k',X[11]:'l',X[12]:'m',X[13]:'n',X[14]:'o',X[15]:'p',X[16]:'q',X[17]:'r',X[18]:'s',X[19]:'t',X[20]:'u',X[21]:'v',X[22]:'w',X[23]:'x',X[24]:'y',X[25]:'z'}
N = int(input())
inputed = []
output = []
mapping = {}
for _ in range(N):
    S = input()
    inputed.append(S)
    tmp = []
    for s in S:
        tmp.append(dict[s])
    output.append(''.join(tmp))
#pdb.set_trace()
for oup, inp in zip(output, inputed):
    mapping[oup] = inp
#pdb.set_trace()
for key in sorted(mapping):
    print(mapping[key])

