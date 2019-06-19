class Solution:
	def search(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""
		#寻找数组中的最小数字
		def find_rotate_index(left, right):
			#如果数组没有旋转，那返回的下标就是0，就是该数组的最小值下标
			if nums[left] < nums[right]:
				return 0

			while left <= right:
				pivot = (left + right) // 2
				if nums[pivot] > nums[pivot + 1]:
					return pivot + 1
				else:
					#如果利用left和mid比较，left<mid，则说明mid位于大的那半区，否则说明位于小的半区。
					if nums[pivot] < nums[left]:
						right = pivot - 1
					else:
						left = pivot + 1

		def search(left, right):
			"""
			Binary search
			"""
			while left <= right:
				pivot = (left + right) // 2
				if nums[pivot] == target:
					return pivot
				else:
					if target < nums[pivot]:
						right = pivot - 1
					else:
						left = pivot + 1
			return -1

		n = len(nums)
		"""需要做特殊情况的判断，比如数组长度为0；数组长度为1；数组没有旋转
		"""
		if n == 0:
			return -1
		if n == 1:
			return 0 if nums[0] == target else -1

		rotate_index = find_rotate_index(0, n - 1)

		# if target is the smallest element
		if nums[rotate_index] == target:
			return rotate_index
		# if array is not rotated, search in the entire array
		if rotate_index == 0:
			return search(0, n - 1)
		if target < nums[0]:
			# search on the right side
			return search(rotate_index, n - 1)
		# search on the left side
		return search(0, rotate_index)




solution =Solution()
print(solution.search([4,5,6,7,0,1,2],0))


