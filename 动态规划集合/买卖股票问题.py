class Solution(object):
	def maxProfit(self,nums):
		length = len(nums)
		if length <=1:return 0
		minNum = nums[0]
		cur_max = 0
		dp = []
		dp.append(0)

		for i in range(1,length):
			#如果当前数值小于之前最小值，那么最大收益一定和之前cur_max相同，用min记录minNum
			if nums[i] <=minNum:
				dp.append(cur_max)
				minNum = nums[i]
			else:
				if (nums[i]-minNum) >cur_max:
					dp.append(nums[i]-minNum)
					cur_max = nums[i]-minNum
				else:
					dp.append(cur_max)

		return dp[-1]

solution = Solution()
print(solution.maxProfit([1,2]))