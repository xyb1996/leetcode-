"""
问题描述：给定一个表示分数的非负整数数组。 玩家1从数组任意一端拿取一个分数，随后玩家2继续从剩余数组任意一端拿取分数，
然后玩家1拿，……。每次一个玩家只能拿取一个分数，分数被拿取之后不再可取。直到没有剩余分数可取时游戏结束。
最终获得分数总和最多的玩家获胜。

给定一个表示分数的数组，预测玩家1是否会成为赢家。你可以假设每个玩家的玩法都会使他的分数最大化。

输入: [1, 5, 233, 7]
输出: True
"""

"""思路：dp[i][j]表示从数组下标[i]到[j]之间的数组选择先拿哪个时，玩家一比玩家二多获得的分数
很多这种一维数组选取最优解的题目都可以转化成这种二维的动态规划问题

我的想法是从规模为n到1这样的情况考虑，玩家1先选择一个大的，玩家二再选，这样肯定只是局部最优的，不是全局最优的
如果要全局最优肯定要从规模从1到n这样来考虑。使用动态规划的思想
"""
n = int(input())
a= []
for i in range(n):
	tmp = int(input())
	a.append(tmp)

def win(num,n):
	dp=[[0]*n for _ in range(n)]

	#初始化，如果数组长度为1，那么先手一定比后手多num[i]
	#否则，如果先手选择i,那么先手比后手多num[i]-dp[i+1][j]
		#  如果先手选择j，那么先手比后手多num[j]-dp[i][j-1]
		# 返回其中大着
	for i in range(n):
		dp[i][i] = num[i]

	# x 表示问题规模
	for x in range(1,n):

		for j in range(x,n):
			i = j-x
			left = num[i]-dp[i+1][j]
			right = num[j]-dp[i][j-1]
			dp[i][j] = max(left,right)
	return dp[0][n-1]

ans  = 0

for i in range(n):
	ans = max(ans,win(a[i:]+a[:i],n))

print(ans)






