#问题描述：
"""小明同学在参加一场考试，考试时间2个小时。试卷上一共有n道题目，小明要在规定时间内，完成一定数量的题目。
考试中不限制试题作答顺序，对于 i 第道题目，小明有三种不同的策略可以选择:  (1)直接跳过这道题目，不花费时间，本题得0分。

(2)只做一部分题目，花费pi分钟的时间，本题可以得到ai分。  (3)做完整个题目，花费qi分钟的时间，本题可以得到bi分。

小明想知道，他最多能得到多少分。
第一行输入一个n数表示题目的数量。

接下来n行，每行四个数p_i，a_i，q_i，b_i。(1≤n≤100，1≤p_i≤q_i≤120，0≤a_i≤b_i≤1000
)。

输出一个数，小明的最高得分。

做前面n-1个题目可能的得分数
"""

n = int(input())
p=[]
a = []
q = []
b = []
for i in range(n):
	line = [int(i) for i in input().split()]
	p.append(line[0])
	a.append(line[1])
	q.append(line[2])
	b.append(line[3])

res = 0
dp = [ [0]*(n+1) for i in range(120+1)]#一个121*n+1大小的二维矩阵

# for i in range(120):
# 	if i >=p[0]:
# 		dp[i][0] = a[0]
# 	elif i>= q[0]:
# 		dp[i][0] = b[0]

# dp[i][j]表示在时间i内给定j个任务，最多能得到多少分。
for i in range(1,120+1):
	for j in range(1,n+1):
		#如果给的时间能够完成整个题目，那么最优情况对应着三种情况的最大值。可以选择不做，或做一半，做全部
		if i >=q[j-1]:
			dp[i][j] = max(dp[i][j - 1], dp[i - p[j-1]][j - 1] + a[j-1], dp[i - q[j-1]][j - 1] + b[j-1])
		elif i >=p[j-1]:
			dp[i][j] = max(dp[i][j - 1], dp[i - p[j - 1]][j - 1] + a[j - 1])
		#否则时间不够完成部分题目，那么得分等于dp[i][j-1]
		else:
			dp[i][j] = dp[i][j-1]

print(dp[-1][-1])



