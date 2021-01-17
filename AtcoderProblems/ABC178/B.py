a,b,c,d = map(int, input().split())

choise= []
choise.append(a*c)
choise.append(a*d)
choise.append(b*c)
choise.append(b*d)
print(max(choise))
