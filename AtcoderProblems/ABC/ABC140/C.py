import pdb

#　サンプルを参考にそれっぽくやったら通った（こういう問題は面白くない）
n = int(input())
b = list(map(int, input().split()))
output = []
output.append(b[0])
for i in range(len(b)-1):
    output.append(min(b[i], b[i+1]))
output.append(b[-1])
print(sum(output))
