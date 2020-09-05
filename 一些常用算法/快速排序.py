"""
快速排序，paritition 非递归版本实现，
"""

def quicksort(alist,start,end):
	#如果只剩一个或0个元素，返回
	if start>=end:
		return

	m = start
	for i in range(start+1,end+1):
		#因为m记录的是从左往右的第一个大于start的下标的前面一个位置
		#如果alist[i]小于中枢元素，那么肯定被交换到前面了
		if alist[i] <alist[start]:
			m+=1
			alist[i],alist[m] = alist[m],alist[i]
	alist[start],alist[m] = alist[m],alist[start]
	quicksort(alist,start,m-1)
	quicksort(alist,m+1,end)


unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
quicksort(unsortedArray, 0, len(unsortedArray) - 1)
print(unsortedArray)
