import random
class Solution:

	def __init__(self, nums):
		self.init = list(nums)
		self.nums = nums
		self.length = len(nums)
	def reset(self) -> [int]:
		"""
		Resets the array to its original configuration and return it.
		"""
		self.nums = list(self.init)
		return self.nums

	def shuffle(self):
		"""
		Returns a random shuffling of the array.
		:rtype: List[int]
		"""
		for i in reversed(range(self.length)):
			index = random.randint(0, i)
			self.nums[i], self.nums[index] = self.nums[index], self.nums[i]
		return self.nums


"""这个题目下面的提示reset和shuffle都赋值了，所以这两个函数是需要返回变量的。"""
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

