"""
问题描述：Given a collection of distinct integers, return all possible permutations.
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution(object):
	def backtrack(self,rtlist,tmplist,nums):
		if len(tmplist) ==len(nums):
			#注意，如果不赋值副本过来，赋值过来的是tmplist的最终结果，也就是‘[]’
			rtlist.append(tmplist[:])
			return

		for i in nums:
			if i in tmplist:
				continue
			tmplist.append(i)
			self.backtrack(rtlist,tmplist,nums)
			tmplist.pop()

	def permutations(self,nums):
		rtlist = []
		tmplist = []
		self.backtrack(rtlist,tmplist,nums)
		return rtlist

solution = Solution()
print(solution.permutations([1,2,3]))
