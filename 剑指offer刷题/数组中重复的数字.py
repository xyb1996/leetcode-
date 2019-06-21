#1.长度为n的数组所有数字都在0～n-1范围内，不知道有几个数字重复了，找出任意重复的一个数字
"""法一：利用哈希表，解决；法二如下，利用交换"""
def duplicate(nums):
	length = len(nums)
	#别忘了临界值判断，-1表示没找到。
	if length ==0:
		return -1
	index = 0
	while index <=length-1:
		if nums[index] ==index:
			index+=1
		else:
			#将值为nums[i]的数放到下表为nums[i]下面
			"""千万注意这里面不要用nums[nums[index]],nums[index] =nums[index],nums[nums[index]]
			这样直接交换，因为这样在第二个赋值的时候改变了nums[i]的值，这里是个坑，老子被坑过"""
			if nums[index] !=nums[nums[index]]:
				tmp = nums[index]
				nums[index] =nums[tmp]
				nums[tmp] = tmp
			else:
				return nums[index]

print(duplicate([2,3,1,0,2,5,3]))

#2、题目进阶，不修改数组，找出重复数字,要求1-n范围内的数字有n+1个：

def getDuplication(nums):
	def countNumber(nums,start,end):
		if len(nums) ==0:
			return 0
		count=0
		for i in range(len(nums)):
			if nums[i]>=start and nums[i] <=end:
				count+=1
		return count
	length = len(nums)
	#边界判断
	if length ==0:
		return -1
	start = 1
	end = length-1
	while start <=end:
		mid = (start+end) //2
		count = countNumber(nums,start,mid)
		if start == end:
			if count >1:
				return start
		#注意这里是mid，不是mid-1，意思是如果start-mid之间的数字个数大于mid-start+1，则去start-mid中去继续二分查、找
		if count >mid-start+1:
			end =mid
		else:
			start = mid+1
		#否则返回不存在重复数组
	return -1

print(getDuplication([2,3,5,4,3,2,6,7]))
