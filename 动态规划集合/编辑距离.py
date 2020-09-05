"""
题目描述：
给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

示例 1:

输入: word1 = "horse", word2 = "ros"
输出: 3
解释:
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')


"""
#从word1的一部分单词到word2的一部分单词的编辑距离
#dp[i][j]表示的是从word1[0][i-1]到word2[0][j-1]的最短编辑距离
class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		if not word1 or not word2:
			return len(word1)+len(word2)
		m = len(word1)
		n = len(word2)
		dp = [ [0]*(n+1) for _ in range(m+1)]
		for i in range(1,n+1):
			dp[0][i] = dp[0][i-1]+1
		for j in range(1,m+1):
			dp[j][0] = dp[j-1][0]+1

		for i in range(1,m+1):
			for j in range(1,n+1):
				if word1[i-1] == word2[j-1]:
					dp[i][j] =dp[i-1][j-1]
				else:
					dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
		return dp[-1][-1]