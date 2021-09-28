import pdb
C = [list(map(int, input().split())) for _ in range(3)]

for a1 in range(101):
    for a2 in range(101):
        for a3 in range(101):
            b1 = C[0][0]-a1
            b2 = C[0][1]-a1
            b3 = C[0][2]-a1
            if a1+b1==C[0][0] and a1+b2==C[0][1] and a1+b3==C[0][2] and \
                a2+b1 == C[1][0] and a2+b2==C[1][1] and a2+b3==C[1][2] and \
                a3+b1 == C[2][0] and a3+b2==C[2][1] and a3+b3==C[2][2]:
                print('Yes')
                exit()
print('No')

