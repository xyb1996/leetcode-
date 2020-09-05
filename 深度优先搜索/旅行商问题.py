#旅行商问题，用的dfs做的，但是时间复杂度太高了。


n = int(input())
cost = []
mincost = float('inf')
trace={}

for i in range(n):
	cost.append([])
	line = list(map(int,input().split()))
	for j in range(n):
		cost[i].append(line[j])



def dfs(idx,cur):
	global mincost
	if len(trace) ==n:
		mincost = min(mincost,cur)
		return


	for i in range(n):
		if len(trace) <n-1 and i ==0:continue
		if i not in trace:
			trace[i] =1
			cur+= cost[idx][i]
			dfs(i,cur)
			cur -= cost[idx][i]
			trace.pop(i)

dfs(0,0)
print(mincost)

#动态规划的解法
n = 4 #城市数量
roadInfo = [[0]*n for _ in range(n)]

dp = [ [0x7ffff]*(1 << n-1 ) for i in range(n)]

for i in range(n):
	dp[i][0] = roadInfo[i][0]

for j in range(1 << n-1):
	for i in range(n):
		dp[i][j] = 0x7ffff
		if j >>(i-1) &1 ==1:   #如果j的第i位是1表示i已经被访问过了
			continue
		for k in range(1,n):
			if (j >>(k-1)) & 1 ==0:
				continue       #不能到达k，则continue
			if dp[i][j] > roadInfo[i][k] + dp[k][j ^ (1 << (k - 1))]:
				dp[i][j] = roadInfo[i][k] + dp[k][j ^ (1 << (k - 1))]

