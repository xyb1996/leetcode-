# class Solution:
# 	def combinationSum(self, candidates, target: int):
# 		result = []
# 		def backtrace(candidates=candidates,target=target,tmp=[]):
# 			if target == 0:
# 				result.append(tmp)
# 				return
# 			for i in candidates:
# 				if (target-i)>=0:
# 					backtrace(candidates,target-i,tmp+[i])
# 				else:
# 					break
# 		candidates = sorted(candidates)
# 		backtrace()
# 		return result
"""
注意对比我一开始的代码和人家的代码，我的代码中没有排除多余的组合，即2,2,3和3,2,2都返回出去了。
看看人家，就知道了在backtrace时传入i，在利用for j in range(i,n) 那么进行深度优秀搜索的时候就只考虑i下标后的元素。
"""
#
#
class Solution:
	def combinationSum(self, candidates, target: int):
		candidates.sort()
		n = len(candidates)
		res = []

		def backtrack(i, tmp_sum, tmp):
			if tmp_sum > target or i == n:
				return
			if tmp_sum == target:
				res.append(tmp)
				return
			for j in range(i, n):
				if tmp_sum + candidates[j] > target:
					break
				backtrack(j, tmp_sum + candidates[j], tmp + [candidates[j]])

		backtrack(0, 0, [])
		return res

"""这种模板也比较好，可以参考下，就是说下条路继续走这条路，or下条路走其他选择了"""
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []
        def helper(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            helper(i,  tmp_sum + candidates[i],tmp + [candidates[i]])
            helper(i+1, tmp_sum ,tmp)
        helper(0, 0, [])
        return res




solution = Solution()
print(solution.combinationSum([2,3,6,7],7))



