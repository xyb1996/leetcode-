class Solution:
	def combinationSum2(self, candidates, target: int):
		result = []
		n = len(candidates)
		candidates = sorted(candidates)
		used = [False]*n
		def backtrace(i,tmp_target,tmp):

			if tmp_target >target or i ==n:
				return
			if tmp_target == target:
				if tmp not in result:
					result.append(tmp)
				return
			for j in range(i,n):

				if used[j]:
					continue
				used[j] =True

				backtrace(j,tmp_target+candidates[j],tmp+[candidates[j]])
				used[j] =False
		backtrace(0,0,[],0)
		return result


#以上是我的思路，有点不太好，应该这样
class Solution:
	def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
		if not candidates:
			return []
		candidates.sort()
		n = len(candidates)
		res = []

		def backtrack(i, tmp_sum, tmp_list):
			if tmp_sum == target:
				res.append(tmp_list)
				return
			for j in range(i, n):
				if tmp_sum + candidates[j] > target: break
				if j > i and candidates[j] == candidates[j - 1]: continue
				backtrack(j + 1, tmp_sum + candidates[j], tmp_list + [candidates[j]])

		backtrack(0, 0, [])
		return res


solution = Solution()
print(solution.combinationSum2([2,5,2,1,2],5))

