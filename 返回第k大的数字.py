#一般面试官不会满足这种答案
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums)[-k]

#这里借鉴快速排序的思想
class Solution2:
	def findKthLargest(self,nums,k):
		pivot = nums[0]
		l = [i for i in nums if i > pivot]
		m = [i for i in nums if i == pivot]
		r = [i for i in nums if i < pivot]
		if k<=len(l):
			return self.findKthLargest(l,k)
		elif k<=len(l)+len(m):
			return pivot
		else:
			return self.findKthLargest(r,k-len(l)+len(m))
