"""
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
例如，给定三角形：

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
"""

class Solution(object):
	def minimumTotal(self, triangle):
		length = len(triangle)

		if length ==1:
			return triangle[0][0]

		dp = [[triangle[0][0]]]
		for i in range(1,length):
			dp.append([])
			for j in range(len(triangle[i])):

				if j ==0:
					dp[i].append(dp[i-1][j]+triangle[i][j])
				elif j == len(triangle[i]) - 1:
					dp[i].append(dp[i - 1][j - 1] + triangle[i][j])
				else:
					#                     当前取值，在上一层的邻边最小值相加
					dp[i].append(min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j])
		return min(dp[(length-1)])

solution = Solution()
print(solution.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))

