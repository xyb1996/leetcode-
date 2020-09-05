import  itertools
#迭代的方法：大致思想就是先生成包括一个数字的列表，然后利用已经生成的列表中的每个
#元素与当前的数字组合得到长度多1个的数字组合。
class Solution:
	def subsets(self, nums):
		res = [[]]
		for i in nums:
			res = res+[temp+[i] for temp in res]

		return res
#回溯算法思想:
	#回溯算法的关键就是不合适就退一步，增加约束限制条件，减少复杂度。


	def subsets2(self, nums):
		res = []
		n = len(nums)

		def helper(i,tmp):
			res.append(tmp)
			#注意这里的range（i,n）就是隐含的递归边界，就是当长度为n时，就不再组合起来。返回长度为2的情况
			#继续组合。
			for j in range(i,n):
				helper(j+1,tmp+[nums[j]])

		helper(0,[])
		return res

solution  = Solution()
print(solution.subsets2([1,2,3]))
