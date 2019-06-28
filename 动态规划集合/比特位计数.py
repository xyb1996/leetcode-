"""
问题描述： 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
输入: 5
输出: [0,1,1,2,1,2]
"""
#好好体会这道题的dp思想，
def count_Bit(num):
	dp=[]
	k = 0
	dp.append(0)

	for i in range(1,num+1):
		#如果i是整数幂，那么1的个数一个是1
		if i == 2**k:
			dp.append(1)
			k+=1
		#否则的话，dp[i]=最高位的1+出去最高位1剩余数字中的1的个数
		else:
			dp.append(1+dp[i-2**k])
	return dp