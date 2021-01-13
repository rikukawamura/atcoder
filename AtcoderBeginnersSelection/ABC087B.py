A = int(input())
B = int(input())
C = int(input())
X = int(input())

list_A = []
list_B = []
list_C = []

for i in range(A+1):
    list_A.append(500*i)

for i in range(B+1):
    list_B.append(100*i)

for i in range(C+1):
    list_C.append(50*i)


count = 0

for i in list_A:
    for j in list_B:
        for k in list_C:
            if (i+j+k) == X:
                count += 1

print(count)