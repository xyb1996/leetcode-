"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。

"""

#二维数组dp
class Solution:
	def minPathSum(self, grid) :
		m = len(grid)
		if m == 0:
			return 0
		n = len(grid[0])
		dp = [ [0]*n for i in range(m)]
		dp[0][0] = grid[0][0]
		for i in range(1,n):
			dp[0][i] = grid[0][i]+dp[0][i-1]
		for i in range(1,m):
			dp[i][0] = grid[i][0]+dp[i-1][0]
		for i in range(1,m):
			for j in range(1,n):
				dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
		return dp[m-1][n-1]

#一维数组dp
class Solution2:
	def minPathSum(self, grid) :
		m = len(grid)
		if m == 0:
			return 0
		n = len(grid[0])
		dp =  [0]*n
		dp[0] = grid[0][0]
		for i in range(1,n):
			dp[i] = grid[0][i]+dp[i-1]
		for i in range(1,m):
			for j in range(n):
				if j == 0:
					dp[j] = dp[j]+grid[i][j]
				else:
					dp[j] = min(dp[j],dp[j-1])+grid[i][j]
		return dp[-1]
