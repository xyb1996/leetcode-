class Solution:
    """
    1、暴力法：从头开始遍历每一种可能，具体解释看下面的if解释
    tmp记录当前的遍历的序列和，max_记录最大的子序和
    """
    def maxSubArray(self, nums: List[int]) -> int:
        tmp = nums[0]
        max_ = tmp
        n = len(nums)
        for i in range(1,n):
        #如果当前序列加上当前遍历的数字>nums[i]，则当前序列继续向后遍历，比较当前序列和最大序列和，赋给最大值
            if tmp + nums[i]>nums[i]:
                max_ = max(max_, tmp+nums[i])
                tmp = tmp + nums[i]
            else:
		#如果符合这种情况，则当前序列直接从nums[i]重新开始，并比较最大值赋值给max_
                max_ = max(max_, tmp, nums[i])
                tmp = nums[i]
        return max_

#2、采用分治法解决
class Solution2:
	def maxSubArray(self, nums: List[int]) -> int:
		n = len(nums)
		# 递归终止条件
		if n == 1:
			return nums[0]
		else:
			# 递归计算左半边最大子序和
			max_left = self.maxSubArray(nums[0:len(nums) // 2])
			# 递归计算右半边最大子序和
			max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

		# 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
		max_l = nums[len(nums) // 2 - 1]
		tmp = 0
		for i in range(len(nums) // 2 - 1, -1, -1):
			tmp += nums[i]
			max_l = max(tmp, max_l)
		max_r = nums[len(nums) // 2]
		tmp = 0
		for i in range(len(nums) // 2, len(nums)):
			tmp += nums[i]
			max_r = max(tmp, max_r)
		# 返回三个中的最大值
		return max(max_right, max_left, max_l + max_r)
#3、利用动态规划，自底向上的计算最大子数组和
class Solution:
	#计算以i为下标结尾的最大连续子数组的值
	def maxSubArray(self, nums):
		n = len(nums)
		if n == 0:
			return 0
		if n == 1:
			return nums[0]
		dp = [0] * n
		dp[0] = nums[0]

		for i in range(1, n):
			if dp[i - 1] + nums[i] > nums[i]:
				dp[i] = dp[i - 1] + nums[i]

			else:
				dp[i] = nums[i]

		max_ = dp[0]
		for i in dp:
			if i > max_:
				max_ = i
		return max_