import  itertools
#迭代的方法：大致思想就是线生成包括一个数字的列表，然后利用已经生成的列表中的每个
#元素与当前的数字组合得到长度多1个的数字组合。
class Solution:
	def subsets(self, nums):
		res = [[]]
		for i in nums:
			res = res+[temp+[i] for temp in res]

		return res
"""回溯算法思想:
	回溯算法的关键就是不合适就退一步，增加约束限制条件，减少复杂度。"""

	def subsets(self, nums: List[int]) -> List[List[int]]:
		res = []
		n = len(nums)

		def helper(i,tmp):
			res.append(tmp)
			for j in range(i,n):
				helper(j+1,tmp+[nums[j]])

		helper(0,[])
		return res

solution  = Solution()
print(solution.subsets([1,2,3]))
