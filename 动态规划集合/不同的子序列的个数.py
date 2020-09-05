"""
题目描述：
给定一个字符串 S 和一个字符串 T，计算在 S 的子序列中 T 出现的个数。

一个字符串的一个子序列是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）

例子：
输入: S = "rabbbit", T = "rabbit"
输出: 3

"""
#说实话这个dp还是比较不容易想到的
#dp[i][j]表示T字符串中前i个字符可以有S j个字符通过删除一些字符的获得的个数

class Solution:
	def numDistinct(self, s: str, t: str) -> int:
		m = len(s)
		n = len(t)

		dp  = [[0]*(m+1) for _ in range(n+1)]

		#第一行表示t是空字符串，对于s长度任意来说无疑都是1
		for i in range(m+1):
			dp[0][i] = 1

		for i in range(1,n+1):
			for j in range(1,m+1):
				if s[j-1] == t[i-1]:
					dp[i][j] = dp[i-1][j-1]+dp[i][j-1]
				else:
					dp[i][j] = dp[i][j-1]
		return dp[-1][-1]