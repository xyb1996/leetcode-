
k, n = [int(i) for i in input().split()]

num = []
for i  in range(n):
	num.append([])
	line  = [int(_) for _ in input().split()]
	for j in range(n):
		num[i].append(line[j])


# 方法1，二分套二分，时间复杂度O(n * logn * logn)
def binary_search(num,mid):
	i = 0
	j = len(num)-1

	while i<=j:
		mid = (i+j) >>1
		if num[mid] <mid:
			i = mid+1
		else:
			j = mid-1
	return i

low = num[0][0]
high = num[n-1][n-1]
count  = 0

while low <=high:
	count = 0
	mid = (low+high)>>1
	for i in num:
		count+=binary_search(i,mid)
	if count <k:
		low=mid+1
	else:
		high = mid-1

print( low)


