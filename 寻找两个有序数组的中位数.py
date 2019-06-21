#用O(log(min(m,n))算法
"""
首先要理解数组中的中位数的概念，指的是将数组分成长度相等的两部分，且
有一半的数组元素都大于另一半数组的元素。那么可以考虑二分法去解决
"""
def findMedianSortedArrays(A,B):
	m= len(A)
	n= len(B)
	#要确保n>m
	if m >n:
		m,n,A,B = n,m,B,A
	if n ==0:
		raise ValueError
	i_min = 0
	i_max = m
	#i+j就是左半部分的长度，这一步保证了左边长度等于右边
	half_len = (m+n+1) //2
	while i_min<=i_max:
		i = (i_min+i_max) //2
		j = half_len-i
		#如果i太小要让i递增，并且不能超过m
		if i<m and A[i] <B[j-1]:
			i_min = i+1
		#i太大，让它减小，并不能小于n
		elif i>0 and A[i-1]>B[j]:
			i_max = i-1
		#否则，i就是我们要求的
		else:
			#考虑边界问题，以免数组越界
			if i ==0:
				left_max = B[j-1]
			elif j ==0:
				left_max = A[i-1]
			else:
				left_max = max(A[i-1],B[j-1])

			if (m+n) %2 ==1:
				return left_max
			else:
				if i ==m:
					right_max = B[j]
				elif j==n:
					right_max = A[i]
				else:
					right_max = min(A[i],B[j])

				return (left_max+right_max) /2