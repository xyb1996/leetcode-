"""解题思路：从0-n-2，从0开始偷到n-2 和从1偷到n-1开始，看两个数组哪个偷的多"""
class Solution:
	def rob(self, nums: [int]):
		length = len(nums)
		if length ==0:return 0
		if length ==1:return nums[0]
		if length ==2:return max(nums)

		dp1  = [0]*length
		dp2 = [0] * length

		#0-n-2:
		dp1[0] = nums[0]
		dp1[1] =max(nums[0],nums[1])

		for i in range(2,length-1):
			dp1[i] = max(dp1[i-2]+nums[i],dp1[i-1])

		dp2[0] =nums[1]
		dp2[1] =max(nums[1],nums[2])
		for j in range(3,length):
			dp2[j-1] = max(dp2[j-3]+nums[j],dp2[j-2])



		return max(dp1[length-2],dp2[length-2])

solution = Solution()
print(solution.rob([1,2,3,1]))
