"""
题目：我们有很多区域，每个区域都是从a到b的闭区间，现在我们要从每个区间中挑选至少2个数，那么最少挑选多少个？

输入：第一行是N（N<10000）,表示有N个区间，之间可以重复
然后每一行是ai,bi，持续N行，表示现在区间。均小于100000

输出：输出一个数，代表最少选取数量。

样例：
4
4 7
2 4
0 2
3 6

输出：4

"""

n = int(input())
a_b = []
for i in range(n):
	line = list(map(int,input().split()))
	a_b.append((line[0],line[1]))
#按区间右端点排序
a_b.sort(key=lambda x :x[1])
#初始选择的区间是右端点以及左边的一个点

res = 2
a,b = a_b[0][1]-1,a_b[0][1]


for i in range(1,n):

	c,d = a_b[i]
	if c > b:
		res += 2
		a, b = d-1, d
	elif c >= a and d <= b:
		continue
	elif c == b:
		res += 1
		a, b = b, d
	#因为是按照d来排序的，所以如果出现这种情况，肯定是

	#其实对于其他的情况来说也是a，b不变，res不增加
print(res)



#另外一种解法，更通用。
import sys

n = sys.stdin.readline().strip()
n = int(n)
temp = []
sol = []
for i in range(n):
	l = list(map(int, sys.stdin.readline().strip().split()))
	temp.append(l[::-1])
temp.sort()
sol.append(temp[0][0] - 1)
sol.append(temp[0][0])
for i in range(n - 1):
	#如果有一个区间的左端点在上一个区间之中，那么这个ans加上区间右端点
	#原理就是下一个区间的左端点在上一个区间内，那么这个区间的左端点取上一个区间的右端点。
	if sol[-1] >= temp[i + 1][-1] and sol[-2] < temp[i + 1][-1]:
		sol.append(temp[i + 1][0])
	#如果是小于的情况肯定是加入两个点
	elif sol[-1] < temp[i + 1][-1]:
		sol.append(temp[i + 1][0] - 1)
		sol.append(temp[i + 1][0])
print(len(sol))