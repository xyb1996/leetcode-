"""问题描述：
第一行一个数n(1 <= n <= 105)。
第二行n个数ai(1 <= ai <= 1000)，表示从左往右数第i堆有多少苹果
第三行一个数m(1 <= m <= 105)，表示有m次询问。
第四行m个数qi，表示小易希望知道第qi个苹果属于哪一堆。

输出：m行，第i行输出第qi个苹果属于哪一堆。
输入
5
2 7 3 4 9
3
1 25 11

输出：
1
5
3


思路：主要是时间复杂度的问题，我一开始是从头遍历，后来直接将sum
结果保存在sum1中，再使用二分查找法去查找，效果就更高了。
"""


import bisect

n = int(input())
count = list(map(int,input().split()))
m = int(input())
query = list(map(int,input().split()))
result = []

sum1= []
for index,i in  enumerate(count):
	if index ==0:
		sum1.append(i)
	else:
		sum1.append(sum1[index-1]+i)

for i in query:
	idx = bisect.bisect_left(sum1,i)
	result.append(idx+1)

for i in result:
	print(i)