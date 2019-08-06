"""
输入描述:
一行字符串（由数字0-9，字母a-z、A-Z构成），字条串长度大于0且不大于1000.

输出描述:输出该字符串的最长回文子串的长度。（不要求输出最长回文串，并且子串不要求连续）
"""

#还是利用动态规划思想来求解：
s= input()
n = len(s)
res = 0

#仔细想想其实这样也相当于全部遍历扫描了一遍，不同的是扫描时利用了前面已有的计算信息。效率应该提升了

dp = [ [0]*n for i in range(n)]
for r in range(n):
	dp [r][r] = 1
	for l in reversed(range(0,r)):
		if s[l] ==s[r]:
			dp[l][r] = dp[l+1][r-1]+2
		else:
			dp[l][r] = max(dp[l+1][r],dp[l][r-1])
print(dp[0][n-1])