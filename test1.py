
n = int(input())
pos = []
neg = []
total = 0
for i in range(n):
	line = list(map(float,input().split()))
	if int(line[0]) ==1:
		pos.append(line)
	else:
		neg.append(line)

n = len(pos)
m = len(neg)

for i in range(n):
	for j in range(m):
		if pos[i][1] >neg[j][1]:
			total+=1
		elif pos[i][1]<neg[j][1]:
			total+=0
		else:
			total+=0.5
ans = total / (n*m)
print('%.2f'%ans)