#法一：回溯法,好像时间通不过
class Solution1:
	def canJump(self, nums:[int]) -> bool:
		length = len(nums)
		flag1 =False
		def backtrace(k):

			if k  >=length-1:
				return True

			for i in reversed(range(nums[k])):
				flag2 = backtrace(k+i+1)
				if flag2:
					return True

			return False
		flag1 = backtrace(0)
		return flag1
solution = Solution1()
print(solution.canJump([3,2,1,0,4]))

#自底向上的动态规划，还是超时了
class Solution:
	def canJump(self, nums:[int]) -> bool:
		length = len(nums)
		dp = [False]*(length-1)+[True]
		for i in reversed(range(length-1)):
			for j in range(nums[i]):
				if dp[j+1+i] ==True:
					dp[i] =True
					break
		return dp[0]
solution2 = Solution()
print(solution2.canJump([3,2,1,0,4]))

class Solution3:
	def canJump(self, nums:[int]) -> bool:
		length = len(nums)
		last = length-1
		for i in reversed(range(length-1)):
			if i+nums[i] >=last:
				last = i
		return last ==0