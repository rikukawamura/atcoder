import pdb

N=int(input())
Q=[]

for i in range(N):
	w=int(input())
	ok=0
	pdb.set_trace()
	for j in range(len(Q)):
		if w<=Q[j]:
			ok=1
			Q[j]=w
			break
	if ok==0:
		Q.append(w)
	Q.sort()

print(len(Q))

