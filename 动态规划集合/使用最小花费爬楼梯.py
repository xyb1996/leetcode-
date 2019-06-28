class Solution(object):
	def minCostClimbingStairs(self, cost):
		"""
		:type cost: List[int]
		:rtype: int
		"""
		#        思路： 从楼顶分析，比如说10为楼顶，到达楼顶只有两种方式，一种从第八层走两步到达，一种是从第九层走一步到达，因为该10为楼顶其：
		#       10为楼顶：F(10)最有子结构为:  F(9) 和  F(8)
		#                   F（10） 递推式： F(10)=min(F(9)+cost[9],F(8)+cost[8])
		#                            边界:  F(0)=1  F(1)=100
		#

		if len(cost) <= 1:
			return min(cost)
		dp = []
		dp.append(cost[0])
		dp.append(cost[1])
		for i in range(2, len(cost) + 1):  # 楼顶不在cost的范围内，因为对遍历+1
			if i == len(cost):  # 该层为楼顶，没有取值
				dp.append(min(dp[i - 1], dp[i - 2]))
			else:
				dp.append(min(dp[i - 1] + cost[i], dp[i - 2] + cost[i]))
		return dp[-1]


solution = Solution()
print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
