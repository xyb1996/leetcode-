class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if len(nums)==0:return [-1,-1]
		if len(nums) ==1:
			if nums[0] == target:
				return [0,0]
			else:
				return [-1,-1]
		low = 0
		high = len(nums)-1
		while low <=high:
			mid = (low+high) //2
			if nums[mid] >=target:
				high = mid -1
			else:
				low = mid+1
		if low ==len(nums):return [-1,-1]
		if nums[high+1] == target:
			begin  = low
		else:
			begin = -1
		low = 0
		high = len(nums)-1
		while low <=high :
			mid =(low +high ) //2
			if nums[mid] <=target:
				low = mid+1
			else:
				high = mid -1

		if nums[low-1] == target:
			end = low-1
		else:
			end = -1
		return [begin,end]
#下面是别人的代码，学习如何改善代码
class Solution:
    # returns leftmost (or rightmost) index at which `target` should be inserted in sorted
    # array `nums` via binary search.
    def extreme_insertion_index(self, nums, target, left):
        lo = 0
        hi = len(nums)

        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo


    def searchRange(self, nums, target):
        left_idx = self.extreme_insertion_index(nums, target, True)

        # assert that `left_idx` is within the array bounds and that `target`
        # is actually in `nums`.
        if left_idx == len(nums) or nums[left_idx] != target:
            return [-1, -1]

        return [left_idx, self.extreme_insertion_index(nums, target, False)-1]


print(solution.searchRange([2,2],3))